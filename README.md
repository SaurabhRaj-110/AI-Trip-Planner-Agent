# Trip Assistant Agent

Trip Assistant is an intelligent, autonomous agent designed to handle complex, multi-day group trip planning. Built with a sleek, dark-themed UI (using Streamlit) and powered by the Gemini API, it dynamically plans itineraries by balancing budgets, energy levels, and time constraints.

It also intelligently replans on the fly when unexpected events occur (e.g., bad weather, someone dropping out, or budget changes) using a deterministic solver to guarantee optimal fairness.

## Features

- **Structured Trip Configuration UI:** Say goodbye to prompting guesswork. Input your travelers, budgets, energy levels, and catalog of activities via sleek, interactive data grids.
- **Cyberpunk / Clean Dark Theme:** A beautiful, responsive chat interface styled with custom CSS, matching modern dark-mode aesthetics.
- **Deterministic Solver Engine:** Under the hood, the agent translates your constraints into a mathematical optimization problem, maximizing group satisfaction within strict time, budget, and energy limits.
- **Dynamic Replanning:** Add unexpected events (like bad weather, someone dropping out, or budget changes) directly to the events grid and instantly recalculate the optimal trip.
- **Local Tool Execution:** Uses Gemini's Tool Calling to execute the Python `solver` locally, ensuring fast, deterministic, and accurate mathematical results while keeping a conversational output.

## Project Structure

```text
trip-agent/
│
├── main.py                 # Streamlit entry point (Template UI & Chat)
├── styles.py               # Custom CSS & HTML templates for the dark theme
├── requirements.txt        # Python dependencies (Streamlit, Pandas, etc.)
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
git clone https://github.com/SaurabhRaj-110/AI-Trip-Planner-Agent.git
cd AI-Trip-Planner-Agent
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

1. **Input:** The user configures the trip parameters (Travelers, Activities, Interruption Events) using the interactive `Trip Configuration Template` tables at the top of the app.
2. **Data Compilation:** Once "Generate Optimal Itinerary" is clicked, the app extracts the pandas dataframe rows and strictly compiles them into the precise textual format required by the deterministic solver.
3. **LLM Delegation:** The compiled string is passed to the `Agent` (powered by Gemini), which recognizes the strict data format and delegates the math to the `calculate_optimal_itinerary` tool.
4. **Solver:** `planner.py` calculates all valid combinations of activities, applies fairness constraints (budget/energy/time), breaks ties lexicographically, and returns the mathematically optimal plan.
5. **Output:** The LLM receives the solver's output, translates it into the styled `// PLAN GENERATED` Markdown format, and displays it in the Streamlit chat UI.

## License

Distributed under the MIT License. See `LICENSE` for more information.
