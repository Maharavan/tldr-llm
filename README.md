# TLDR LLM (AI Summarizer)

Simple Flask web app that sends user text to a Groq Llama 3.3 model and returns a concise TL;DR with configurable length, style, language, and structure.

## Features
- Groq-powered summarization using `llama-3.3-70b-versatile`
- UI controls for length (short/medium/long), style (formal/informal/technical), language (English/Spanish/French), and structure (bullet points/paragraph/numbered list)
- Single-route Flask app with Jinja templates and minimal styling
- Ships with a reusable prompt tuned for concise titles and summaries

## Tech Stack
- Python 3
- Flask
- Groq Python SDK
- Jinja2 templates + CSS

## Project Layout
```
app.py                   # Flask entrypoint and routes
llm.py                   # Groq client and summarize_text helper
prompts.py               # Summarization prompt template
templates/
  tldm/
    base.html
    home.html
    summarize_result.html
  static/
    css/style.css
    image/icon.svg
    image/background.png
requirements.txt
.env                     # define GROQ_API_KEY here (not committed)
```

## Prerequisites
- Python 3.10+ recommended
- Groq API key (https://console.groq.com/)

## Setup
```bash
python -m venv .venv
. .venv/Scripts/activate            # Windows PowerShell: .\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Run
```bash
python app.py
```
Then open http://localhost:5000.

## Usage
1) Paste or type text into the textarea.  
2) Choose length, style, language, and structure from the dropdowns.  
3) Submit to get a titled summary; the result appears on a new page (editable textarea for quick copy/adjust).

## Notes
- The prompt enforces concise output (title + summary only) and respects the selected options.
- Set `temperature` inside `llm.py` (default 0.5) to adjust creativity if desired.
