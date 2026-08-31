"""
TripAI  --  Your smart trip companion
Run with:  python main.py          (auto-launches Streamlit)
   or:     streamlit run main.py
"""
import sys
import os


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
#  STREAMLIT APP
# ═══════════════════════════════════════════════════════════
import streamlit as st
from datetime import datetime
from agent.runner import Agent
from styles import CUSTOM_CSS, HEADER_HTML, WELCOME_HTML, FLOATING_BOT_HTML

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


# ── Quick-action buttons (2-column grid, before first interaction) ──
def _handle_quick_action(text: str):
    """Send a quick-action as a user message and get the agent reply."""
    ts = datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({"role": "user", "content": text, "time": ts})
    with st.spinner("Computing..."):
        try:
            reply = st.session_state.agent.chat_with_user(text)
        except Exception as exc:
            reply = f"Error: {exc}"
    st.session_state.messages.append({"role": "assistant", "content": reply, "time": ts})
    st.rerun()


if not st.session_state.messages:
    # Row 1 — two columns
    c1, c2 = st.columns(2)
    with c1:
        if st.button("\u2728  Best plan for Day 3", key="qa1", use_container_width=True):
            _handle_quick_action("Best plan for Day 3")
    with c2:
        if st.button("\U0001f4c5  What's our plan tomorrow?", key="qa2", use_container_width=True):
            _handle_quick_action("What's our plan for tomorrow?")

    # Row 2 — two columns
    c3, c4 = st.columns(2)
    with c3:
        if st.button("\u25c7  Replan after an event", key="qa3", use_container_width=True):
            _handle_quick_action("Replan after an event")
    with c4:
        if st.button("\U0001f4cb  Check budget summary", key="qa4", use_container_width=True):
            _handle_quick_action("Check budget summary")

    # Row 3 — full width
    if st.button("\u26a1  Check group energy levels", key="qa5", use_container_width=True):
        _handle_quick_action("Check group energy levels")


# ── Chat history ──
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ── Chat input ──
if prompt := st.chat_input("Ask anything about your trip..."):
    ts = datetime.now().strftime("%I:%M %p")

    st.session_state.messages.append({"role": "user", "content": prompt, "time": ts})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Computing optimal itinerary..."):
            try:
                reply = st.session_state.agent.chat_with_user(prompt)
            except Exception as exc:
                reply = f"Error: {exc}"
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply, "time": ts})


# ── Floating chat icon ──
st.markdown(FLOATING_BOT_HTML, unsafe_allow_html=True)