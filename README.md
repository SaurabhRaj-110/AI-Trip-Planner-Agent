# TripAI Agent

![TripAI UI Concept](https://img.shields.io/badge/UI-Cyberpunk_Dark_Theme-00ff41.svg?style=flat-square)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)
![Streamlit](https://img.shields.io/badge/streamlit-1.40+-FF4B4B.svg?style=flat-square)

TripAI is an intelligent, autonomous agent designed to handle complex, multi-day group trip planning. Built with a sleek, dark-themed UI (using Streamlit) and powered by the Gemini API, it dynamically plans itineraries by balancing budgets, energy levels, and time constraints.

It also intelligently replans on the fly when unexpected events occur (e.g., bad weather, someone dropping out, or budget changes) using a deterministic solver to guarantee optimal fairness.

## Features

- **Cyberpunk / Clean Dark Theme:** A beautiful, responsive chat interface styled with custom CSS, matching modern dark-mode aesthetics.
- **Natural Language Understanding:** Ask the agent questions normally (e.g., *"What's our plan for tomorrow?"* or *"Bob just dropped out of the trip"*).
- **Deterministic Solver Engine:** Under the hood, the agent translates your constraints into a mathematical optimization problem, maximizing group satisfaction within strict time, budget, and energy limits.
- **Dynamic Replanning:** Adjusts the itinerary instantly if a constraint changes midway through the trip.
- **Local Tool Execution:** Uses Gemini's Tool Calling to execute the Python `solver` locally, ensuring fast and accurate results.

## Project Structure

```text
trip-agent/
│
├── main.py                 # Streamlit entry point & UI layout
├── styles.py               # Custom CSS & HTML templates for the dark theme
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API Keys)
│
├── agent/                  # AI & LLM Logic
│   ├── runner.py           # Gemini API client & tool-calling chat session
│   └── prompts.py          # System prompt & formatting instructions
│
├── solver/                 # Deterministic Logic
│   └── planner.py          # The core itinerary optimization algorithm
│
└── tools/                  # Agent Tools
    └── trip_tool.py        # Exposes the solver to the Gemini model
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/trip-agent.git
cd trip-agent
```

### 2. Create a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application
You can launch the app directly:
```bash
python main.py
```
*(This will automatically trigger `streamlit run main.py` and open the app in your browser at `http://localhost:8501`)*

## How it Works

1. **Input:** The user types a natural language request in the chat UI.
2. **LLM Processing:** The `Agent` (powered by Gemini) parses the constraints and determines if the itinerary needs to be built or updated.
3. **Tool Execution:** If a plan is needed, the LLM calls the `calculate_optimal_itinerary` tool, passing a strict, formalized text format.
4. **Solver:** `planner.py` parses the formatted text, calculates combinations of activities, applies fairness constraints (budget/energy/time), breaks ties lexicographically, and returns the mathematically optimal plan.
5. **Output:** The LLM receives the solver's output, translates it into the styled `// PLAN GENERATED` Markdown format, and displays it in the Streamlit UI.

## License

Distributed under the MIT License. See `LICENSE` for more information.
