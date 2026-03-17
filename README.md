# Task Categorization Agent (Anthropic)

A minimal example of a Python script that reads tasks from a file and uses the Anthropic API to categorize/ prioritize them.

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install anthropic python-dotenv
```

3. Create a `.env` file in the project root with your Anthropic API key:

```env
CLAUDE_API_KEY=sk-...your-key...
```

> The script also checks for `ANTHROPIC_API_KEY` if you prefer that name.

## How to Run

Put your tasks into `task.txt`, one per line.

Run the agent:

```bash
./venv/bin/python taskagent.py
```

## What it does

- Reads `task.txt`
- Sends the list to Anthropic Claude (via the Anthropic SDK)
- Prints a prioritized list of tasks

---

> Note: This is a simple learning example; it does not handle advanced error cases or rate limiting.
