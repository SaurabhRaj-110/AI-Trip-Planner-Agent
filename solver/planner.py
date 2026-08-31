import sys
from itertools import combinations
from dataclasses import dataclass, field
from typing import List, Set, Dict, Tuple

@dataclass
class User:
    name: str
    budget: int
    energy: int
    interests: Set[str]
    active: bool = True

@dataclass
class Activity:
    id: int
    name: str
    cost: int
    duration: int
    energy: int
    tag: str

@dataclass
class Event:
    raw: str
    type: str
    day: int
    target: str = ""
    value: int = 0

class TripSolver:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input.strip().splitlines()
        self.parse_input()

    def parse_input(self):
        lines = [line.strip() for line in self.raw_input if line.strip()]
        idx = 0
        
        self.N, self.D, self.H = map(int, lines[idx].split())
        idx += 1
        
        self.users: Dict[str, User] = {}
        for _ in range(self.N):
            parts = lines[idx].split()
            name, budget, energy, k = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
            interests = set(parts[4:4+k])
            self.users[name] = User(name, budget, energy, interests)
            idx += 1
            
        self.A = int(lines[idx])
        idx += 1
        
        self.activities: Dict[int, Activity] = {}
        for _ in range(self.A):
            parts = lines[idx].split()
            aid, name, cost, dur, energy, tag = int(parts[0]), parts[1], int(parts[2]), int(parts[3]), int(parts[4]), parts[5]
            self.activities[aid] = Activity(aid, name, cost, dur, energy, tag)
            idx += 1
            
        self.events: List[Event] = []
        if idx < len(lines):
            self.E = int(lines[idx])
            idx += 1
            for _ in range(self.E):
                raw_ev = lines[idx]
                parts = raw_ev.split()
                ev_type, day = parts[0], int(parts[1])
                if ev_type == "WEATHER":
                    self.events.append(Event(raw=raw_ev, type=ev_type, day=day, target=parts[2]))
                elif ev_type == "DROP":
                    self.events.append(Event(raw=raw_ev, type=ev_type, day=day, target=parts[2]))
                elif ev_type in ("FATIGUE", "BUDGET"):
                    self.events.append(Event(raw=raw_ev, type=ev_type, day=day, target=parts[2], value=int(parts[3])))
                idx += 1

    def solve_day(self, day: int, users: Dict[str, User], available_act_ids: Set[int], blocked_tags: Set[str]) -> Tuple[List[int], int, int]:
        active_users = [u for u in users.values() if u.active]
        if not active_users:
            return [], 0, 0

        min_budget = min(u.budget for u in active_users)
        min_energy = min(u.energy for u in active_users)

        eligible = [
            self.activities[aid] for aid in available_act_ids 
            if self.activities[aid].tag not in blocked_tags
        ]

        best_choice = None
        # Evaluate empty subset (REST)
        best_key = (0, 0, []) # (-sat, cost, ids)

        for r in range(1, len(eligible) + 1):
            for subset in combinations(eligible, r):
                tot_cost = sum(a.cost for a in subset)
                tot_energy = sum(a.energy for a in subset)
                tot_duration = sum(a.duration for a in subset)

                if tot_cost <= min_budget and tot_energy <= min_energy and tot_duration <= self.H:
                    sat = sum(sum(1 for u in active_users if a.tag in u.interests) for a in subset)
                    ids = sorted(a.id for a in subset)
                    key = (-sat, tot_cost, ids)

                    if best_choice is None or key < best_key:
                        best_key = key
                        best_choice = (ids, tot_cost, sat)

        if best_choice is None:
            return [], 0, 0
        return best_choice

    def run(self) -> str:
        output = ["=== PLAN ==="]
        import copy
        current_users = copy.deepcopy(self.users)
        used_activities = set()
        day_plans = {}

        # 1. Base Plan
        for d in range(1, self.D + 1):
            chosen_ids, cost, sat = self.solve_day(d, current_users, set(self.activities.keys()) - used_activities, set())
            day_plans[d] = (chosen_ids, cost, sat)
            used_activities.update(chosen_ids)
            
            plan_str = " ".join(map(str, chosen_ids)) if chosen_ids else "REST"
            output.append(f"Day {d}: {plan_str} | cost={cost} satisfaction={sat}")

        # 2. Process Events
        for i, ev in enumerate(self.events, 1):
            output.append(f"=== EVENT {i}: {ev.raw} ===")
            # Reconstruct state up to event.day - 1
            sim_users = copy.deepcopy(self.users)
            sim_used = set()

            # Apply previous events that occurred strictly before this event day
            for past_ev in self.events[:i-1]:
                if past_ev.day < ev.day:
                    if past_ev.type == "DROP": sim_users[past_ev.target].active = False
                    elif past_ev.type == "FATIGUE": sim_users[past_ev.target].energy = past_ev.value
                    elif past_ev.type == "BUDGET": sim_users[past_ev.target].budget = past_ev.value

            # Reconstruct activities chosen prior to event day
            for d in range(1, ev.day):
                chosen_ids, _, _ = day_plans[d]
                sim_used.update(chosen_ids)

            # Apply current and subsequent cumulative events for remaining days
            for d in range(ev.day, self.D + 1):
                blocked_tags = set()
                for active_ev in self.events[:i]:
                    if active_ev.day <= d:
                        if active_ev.type == "WEATHER" and active_ev.day == d:
                            blocked_tags.add(active_ev.target)
                        elif active_ev.type == "DROP":
                            sim_users[active_ev.target].active = False
                        elif active_ev.type == "FATIGUE":
                            sim_users[active_ev.target].energy = active_ev.value
                        elif active_ev.type == "BUDGET":
                            sim_users[active_ev.target].budget = active_ev.value

                chosen_ids, cost, sat = self.solve_day(d, sim_users, set(self.activities.keys()) - sim_used, blocked_tags)
                sim_used.update(chosen_ids)
                day_plans[d] = (chosen_ids, cost, sat)
                
                plan_str = " ".join(map(str, chosen_ids)) if chosen_ids else "REST"
                output.append(f"Day {d}: {plan_str} | cost={cost} satisfaction={sat}")

        return "\n".join(output)

def solve(input_data: str) -> str:
    solver = TripSolver(input_data)
    return solver.run()