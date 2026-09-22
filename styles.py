"""
TripAI Agent — Clean Dark Theme
Styles, CSS, and HTML component templates.
"""

# ═══════════════════════════════════════════════════════════
#  CUSTOM CSS
# ═══════════════════════════════════════════════════════════

CUSTOM_CSS = """

/* ===== HIDE STREAMLIT CHROME ===== */
#MainMenu, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}
header[data-testid="stHeader"] {
    background: transparent !important;
}

/* ===== PAGE & LAYOUT ===== */
html, body, .stApp {
    background-color: #080a0e !important;
}

.block-container {
    max-width: 700px !important;
    padding: 0 28px 24px 28px !important;
    margin: 0 auto !important;
}

/* ===== TYPOGRAPHY ===== */
.stApp,
.stApp p,
.stApp label, .stApp li,
.stApp td, .stApp th {
    font-family: 'Georgia Pro', Georgia, 'Noto Serif', 'Times New Roman', serif !important;
    color: #c0c8c0 !important;
}

/* ═══════════════════════════════════════
   HEADER
   ═══════════════════════════════════════ */
.tripai-hdr {
    padding: 22px 0 18px 0;
    position: relative;
}
.tripai-hdr .online {
    color: #00ff41;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.5px;
    margin-bottom: 6px;
}
.tripai-hdr .online .dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: #00ff41;
    border-radius: 50%;
    margin-right: 7px;
    box-shadow: 0 0 6px rgba(0,255,65,0.6);
    vertical-align: middle;
    animation: pulse-dot 2.5s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%,100% { opacity: 1; box-shadow: 0 0 6px rgba(0,255,65,0.6); }
    50% { opacity: 0.5; box-shadow: 0 0 3px rgba(0,255,65,0.3); }
}
.tripai-hdr .title {
    font-family: 'Georgia Pro', Georgia, serif !important;
    font-size: 38px;
    font-weight: 400;
    color: #e8ede8 !important;
    letter-spacing: 1px;
    margin: 4px 0 4px 0;
}
.tripai-hdr .cursor {
    color: #00ff41;
    animation: blink-cursor 1s step-end infinite;
}
@keyframes blink-cursor {
    0%,100% { opacity: 1; }
    50% { opacity: 0; }
}
.tripai-hdr .subtitle {
    font-family: 'Georgia Pro', Georgia, serif !important;
    color: #4a5a4a !important;
    font-size: 14px;
    font-weight: 400;
}
.tripai-hdr .controls {
    position: absolute;
    top: 22px; right: 0;
    color: #3a4a3a;
    font-size: 16px;
    letter-spacing: 14px;
    user-select: none;
}
/* Decorative dots grid */
.tripai-hdr .dots {
    position: absolute;
    top: 42px; right: 70px;
    display: grid;
    grid-template-columns: repeat(4, 8px);
    grid-template-rows: repeat(3, 8px);
    gap: 5px;
}
.tripai-hdr .dots span {
    width: 4px; height: 4px;
    background: #2a3a2a;
    border-radius: 50%;
    display: block;
}

/* ═══════════════════════════════════════
   WELCOME CARD
   ═══════════════════════════════════════ */
.welcome-card {
    background: #12161c;
    border-left: 3px solid #00ff41;
    border-radius: 0 10px 10px 0;
    padding: 20px 24px;
    margin: 8px 0 20px 0;
    max-width: 380px;
}
.welcome-card .greet {
    font-size: 16px;
    color: #d0d8d0 !important;
    margin-bottom: 10px;
    line-height: 1.5;
}
.welcome-card .greet .name {
    color: #00ff41 !important;
    font-weight: 600;
}
.welcome-card .desc {
    font-size: 14px;
    color: #8a9a8a !important;
    line-height: 1.65;
    margin-bottom: 8px;
}
.welcome-card .ask {
    font-size: 14px;
    color: #b0c0b0 !important;
    margin-top: 6px;
}
.welcome-card .wtime {
    font-size: 11px;
    color: #3a4a3a !important;
    margin-top: 12px;
}

/* ═══════════════════════════════════════
   CHAT MESSAGES
   ═══════════════════════════════════════ */
[data-testid="stChatMessage"] {
    background-color: #12161c !important;
    border: none !important;
    border-left: 3px solid #00ff41 !important;
    border-radius: 0 10px 10px 0 !important;
    padding: 16px 20px !important;
    margin-bottom: 12px !important;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] div {
    font-family: 'Georgia Pro', Georgia, serif !important;
    color: #c0ccc0 !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
}

[data-testid="stChatMessage"] strong,
[data-testid="stChatMessage"] b {
    color: #00ff41 !important;
    font-weight: 600 !important;
}

[data-testid="stChatMessage"] h1,
[data-testid="stChatMessage"] h2,
[data-testid="stChatMessage"] h3,
[data-testid="stChatMessage"] h4 {
    color: #00ff41 !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
}

[data-testid="stChatMessage"] code {
    color: #00ff41 !important;
    background: #0d1117 !important;
    padding: 2px 6px !important;
    border-radius: 3px !important;
    font-family: 'Consolas', 'Courier New', monospace !important;
    font-size: 13px !important;
}

[data-testid="stChatMessage"] pre {
    background: #0a0e12 !important;
    border: 1px solid #1a2a1a !important;
    border-radius: 6px !important;
    padding: 14px !important;
}
[data-testid="stChatMessage"] pre code {
    background: transparent !important;
    color: #00ff41 !important;
    font-family: 'Consolas', 'Courier New', monospace !important;
}

/* Tables inside messages (plan stats) */
[data-testid="stChatMessage"] table {
    border-collapse: collapse !important;
    margin-top: 10px !important;
}
[data-testid="stChatMessage"] th {
    color: #5a6a5a !important;
    font-weight: 400 !important;
    font-size: 12px !important;
    text-align: left !important;
    padding: 8px 16px 4px 0 !important;
    border-top: 1px solid #1a2a1a !important;
    border-bottom: none !important;
}
[data-testid="stChatMessage"] td {
    color: #e0e8e0 !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 2px 16px 8px 0 !important;
    border: none !important;
}

[data-testid="stChatMessage"] hr {
    border-color: #1a2a1a !important;
    margin: 10px 0 !important;
}

/* Hide the default avatar icons */
[data-testid="stChatMessage"] img {
    display: none !important;
}
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"],
[data-testid="stChatMessage"] > div:first-child:has(img) {
    display: none !important;
}

/* ═══════════════════════════════════════
   BUTTONS (Quick Actions) — 2-col grid
   ═══════════════════════════════════════ */
.stButton > button {
    background: transparent !important;
    border: 1px solid #1e2e1e !important;
    color: #c0ccc0 !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
    font-size: 13.5px !important;
    font-weight: 400 !important;
    padding: 12px 16px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    border-radius: 8px !important;
    transition: all 0.25s ease !important;
    line-height: 1.4 !important;
}

.stButton > button:hover {
    border-color: #00ff41 !important;
    background: rgba(0, 255, 65, 0.04) !important;
    color: #00ff41 !important;
}

.stButton > button:focus {
    border-color: #00ff41 !important;
    box-shadow: none !important;
}

.stButton > button:active {
    background: rgba(0, 255, 65, 0.08) !important;
}

/* ═══════════════════════════════════════
   CHAT INPUT
   ═══════════════════════════════════════ */
[data-testid="stBottom"],
[data-testid="stBottom"] > div {
    background-color: #080a0e !important;
}

[data-testid="stChatInput"] {
    background-color: #12161c !important;
    border: 1px solid #1e2e1e !important;
    border-radius: 10px !important;
}

[data-testid="stChatInput"] textarea {
    color: #a0b0a0 !important;
    background-color: transparent !important;
    caret-color: #00ff41 !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
    font-size: 14px !important;
}

[data-testid="stChatInput"] textarea:focus {
    border-color: #00ff41 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #3a4a3a !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
}

/* Send button — subtle, not filled */
[data-testid="stChatInput"] button,
[data-testid="stChatInputSubmitButton"] {
    background: transparent !important;
    color: #5a7a5a !important;
    border: none !important;
    transition: color 0.2s !important;
}
[data-testid="stChatInput"] button:hover,
[data-testid="stChatInputSubmitButton"]:hover {
    color: #00ff41 !important;
}

/* ═══════════════════════════════════════
   SPINNER
   ═══════════════════════════════════════ */
.stSpinner, .stSpinner > div,
[data-testid="stSpinner"],
[data-testid="stSpinner"] > div {
    color: #00ff41 !important;
}

/* ═══════════════════════════════════════
   SCROLLBAR
   ═══════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #080a0e; }
::-webkit-scrollbar-thumb { background: #1a2a1a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2a4a2a; }

/* ═══════════════════════════════════════
   EXPANDER & INPUTS
   ═══════════════════════════════════════ */
[data-testid="stExpander"] {
    background: #0d1117 !important;
    border: 1px solid #1e2e1e !important;
    border-radius: 8px !important;
    margin-bottom: 24px !important;
}
[data-testid="stExpander"] summary {
    background: #12161c !important;
    color: #e0e8e0 !important;
    border-bottom: 1px solid #1e2e1e !important;
}
[data-testid="stExpander"] summary p {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #00ff41 !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
}
[data-testid="stExpanderDetails"] {
    padding: 20px !important;
}

/* Number inputs and general inputs inside the template */
.stNumberInput > div > div > input {
    color: #00ff41 !important;
    background: #12161c !important;
    border: 1px solid #1e2e1e !important;
    font-family: 'Consolas', monospace !important;
}
.stNumberInput label {
    color: #a0b0a0 !important;
    font-family: 'Georgia Pro', Georgia, serif !important;
}

/* Dataframe/data_editor */
[data-testid="stDataFrame"] {
    border: 1px solid #1e2e1e !important;
    border-radius: 6px !important;
    overflow: hidden !important;
}
"""


# ═══════════════════════════════════════════════════════════
#  HTML TEMPLATES
# ═══════════════════════════════════════════════════════════

# 12 dots for the decorative grid (3 columns x 2 rows)
_DOTS = '<span></span>' * 6

HEADER_HTML = (
    '<div class="tripai-hdr">'
    '  <div class="online"><span class="dot"></span>ONLINE</div>'
    '  <div class="title">Trip Assistant<span class="cursor"> !! </span></div>'
    '  <div class="subtitle">Your smart trip companion</div>'
    '  <div class="controls">\u2014 \u2715</div>'
    '  <div class="dots">' + _DOTS + '</div>'
    '</div>'
)

# {time} is a .format() placeholder — filled in by main.py
WELCOME_HTML = (
    '<div class="welcome-card">'
    '  <div class="greet">Hey <span class="name">Saurabh!</span> \U0001f44b</div>'
    '  <div class="desc">'
    "    Glad, To see you here<br>"
    '  </div>'
    '  <div class="ask">How can I help you plan your day?</div>'
    '  <div class="wtime">{time}</div>'
    '</div>'
)

FLOATING_BOT_HTML = (
    '<div class="floating-chat">'
    '  <div class="fc-circle">'
    '    <span class="bubble">\U0001f4ac</span>'
    '    <span class="fc-indicator"></span>'
    '  </div>'
    '</div>'
)
