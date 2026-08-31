from solver.planner import solve

def calculate_optimal_itinerary(formatted_input: str) -> str:
    """Calculates the deterministic group trip itinerary and replans around events using fairness constraints and lexicographical tie-breaking.
    
    Args:
        formatted_input: The exact input string matching the format: N D H, user lines, A, activity lines, E, event lines.
    """
    try:
        return solve(formatted_input)
    except Exception as e:
        return f"Error executing planner: {str(e)}"