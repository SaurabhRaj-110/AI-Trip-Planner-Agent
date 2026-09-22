"""
TripAI  --  Your smart trip companion
Run with:  python main.py          (auto-launches Streamlit)
   or:     streamlit run main.py
"""
import sys
import os
import pandas as pd
import streamlit as st
from datetime import datetime
from agent.runner import Agent
from styles import CUSTOM_CSS, HEADER_HTML, WELCOME_HTML

def _running_in_streamlit() -> bool:
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        return get_script_run_ctx() is not None
    except Exception:
        return False

if not _running_in_streamlit():
    import subprocess
    _here = os.path.dirname(os.path.abspath(__file__))
    print()
    print("  [*]  Launching TripAI Agent...")
    print("  -->  Open  http://localhost:8501  in your browser")
    print()
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)],
        cwd=_here,
    )
    sys.exit()


# ═══════════════════════════════════════════════════════════
#  DEFAULT TEMPLATE DATA
# ═══════════════════════════════════════════════════════════

if "default_users" not in st.session_state:
    st.session_state.default_users = pd.DataFrame([
        {"Name": "Alice", "Budget": 100, "Energy": 80, "Interests": "ADVENTURE, FOOD"},
        {"Name": "Bob", "Budget": 80, "Energy": 60, "Interests": "CULTURE, FOOD"},
        {"Name": "Cara", "Budget": 120, "Energy": 70, "Interests": "NATURE, FOOD"},
    ])

if "default_activities" not in st.session_state:
    st.session_state.default_activities = pd.DataFrame([
        {"ID": 1, "Name": "Museum", "Cost": 30, "Duration": 3, "Energy": 20, "Tag": "CULTURE"},
        {"ID": 2, "Name": "Hike", "Cost": 40, "Duration": 5, "Energy": 50, "Tag": "ADVENTURE"},
        {"ID": 3, "Name": "Cafe", "Cost": 20, "Duration": 2, "Energy": 10, "Tag": "FOOD"},
        {"ID": 4, "Name": "Park", "Cost": 25, "Duration": 3, "Energy": 15, "Tag": "NATURE"},
        {"ID": 5, "Name": "Club", "Cost": 50, "Duration": 4, "Energy": 40, "Tag": "NIGHTLIFE"},
    ])

if "default_events" not in st.session_state:
    st.session_state.default_events = pd.DataFrame([
        {"Type": "WEATHER", "Day": 2, "Target": "ADVENTURE", "Value": 0}
    ])


# ═══════════════════════════════════════════════════════════
#  STREAMLIT APP
# ═══════════════════════════════════════════════════════════

# ── Page config ──
st.set_page_config(
    page_title="TripAI",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Inject CSS ──
st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)

# ── Header ──
st.markdown(HEADER_HTML, unsafe_allow_html=True)

# ── Session state ──
if "agent" not in st.session_state:
    st.session_state.agent = Agent()
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Welcome card ──
time_now = datetime.now().strftime("%I:%M %p")
st.markdown(WELCOME_HTML.format(time=time_now), unsafe_allow_html=True)


# ── Trip Configuration Template ──
with st.expander("📝 Trip Configuration Template", expanded=(len(st.session_state.messages) == 0)):
    st.markdown("<div style='color: #8a9a8a; margin-bottom: 20px; font-size: 14px;'>Adjust your trip constraints below. These settings will be parsed strictly to compute the absolute optimal itinerary.</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    days = col1.number_input("Total Days (D)", min_value=1, value=2)
    hours = col2.number_input("Hours per Day (H)", min_value=1, value=8)

    st.write("### 👥 Group Members")
    users_df = st.data_editor(st.session_state.default_users, num_rows="dynamic", use_container_width=True)

    st.write("### 🎟️ Activities Catalog")
    activities_df = st.data_editor(st.session_state.default_activities, num_rows="dynamic", use_container_width=True)

    st.write("### ⚡ Interruption Events (Optional)")
    st.markdown("<div style='color: #8a9a8a; margin-bottom: 10px; font-size: 13px;'>Valid Types: WEATHER, DROP, FATIGUE, BUDGET</div>", unsafe_allow_html=True)
    events_df = st.data_editor(st.session_state.default_events, num_rows="dynamic", use_container_width=True)

    if st.button("⚡ Generate Optimal Itinerary", use_container_width=True):
        ts = datetime.now().strftime("%I:%M %p")
        
        # ── Parse and compile strict string ──
        try:
            lines = [f"{len(users_df)} {days} {hours}"]
            
            for _, row in users_df.iterrows():
                interests_str = str(row['Interests']).replace(',', ' ').strip()
                interests = interests_str.split() if interests_str else []
                lines.append(f"{row['Name']} {row['Budget']} {row['Energy']} {len(interests)} {' '.join(interests)}")
            
            lines.append(str(len(activities_df)))
            for _, row in activities_df.iterrows():
                lines.append(f"{row['ID']} {row['Name']} {row['Cost']} {row['Duration']} {row['Energy']} {row['Tag']}")
            
            # Events
            valid_events = []
            for _, row in events_df.iterrows():
                etype = str(row['Type']).strip()
                if etype: # If not empty
                    val_str = str(int(row['Value'])) if pd.notna(row['Value']) and str(row['Value']) != '0' else ""
                    valid_events.append(f"{etype} {row['Day']} {row['Target']} {val_str}".strip())
                    
            lines.append(str(len(valid_events)))
            lines.extend(valid_events)
            
            raw_input = "\n".join(lines)
            
            # ── Feedback in Chat ──
            user_msg = f"Generate an itinerary for {len(users_df)} travelers over {days} days based on the configuration template."
            st.session_state.messages.append({"role": "user", "content": user_msg, "time": ts})
            
            with st.spinner("Computing mathematical optimum..."):
                reply = st.session_state.agent.chat_with_user(raw_input)
            
            st.session_state.messages.append({"role": "assistant", "content": reply, "time": ts})
            st.rerun()
            
        except Exception as e:
            st.error(f"Configuration Error: {e}. Please check your tables for missing values.")


# ── Chat history (Results) ──
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])