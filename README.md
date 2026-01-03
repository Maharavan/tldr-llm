# tldr-llm

**tldr-llm** is an lightweight LLM-powered web application that generates customizable **TL;DR summaries** from long-form text.  
It allows users to control summary **length**, **style**, **language**, and **structure** through a clean single-page interface.

---

## 🌐 Live Demo

👉 https://summarizer-web-app.onrender.com/

---

## 📦 Repository

👉 https://github.com/Maharavan/tldr-llm

---

## ✨ Features

- Generate concise **TL;DR summaries** from long text
- Customize **summary length**:
  - Short
  - Medium
  - Long
- Choose **summary style**:
  - Formal
  - Informal
  - Technical
- Select **output language**:
  - English
  - Spanish
  - French
- Control **summary structure**:
  - Bullet points
  - Paragraph
  - Numbered list
- Single-page UI with a **single-route Flask backend**
- Prompt-driven LLM summarization

---

## 🧠 How It Works

1. User inputs long-form text.
2. User selects summary preferences:
   - Length
   - Style
   - Language
   - Structure
3. Backend dynamically builds a prompt based on these options.
4. The prompt is sent to the LLM.
5. The generated summary is rendered on the same page.

---

## 🧱 Tech Stack

- Python
- Flask
- LLM API
- HTML + minimal CSS
- Docker
- GitHub Actions
- Render (deployment)

---

## 🗂️ Project Structure

```
tldr-llm/
├── app.py
├── llm.py
├── prompts.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Maharavan/tldr-llm.git
cd tldr-llm
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
Create a `.env` file:
```env
GROQ_API_KEY=your_api_key_here
```

### 4. Start the application
```bash
python app.py
```

Open your browser and visit:
```
http://localhost:5000
```

---
## UI Design

<p align="center">
<img src="screenshots/UI.png" width=100% />
</p>

---
## 🎯 Purpose

This project demonstrates:
- Practical LLM integration in a web application
- Prompt engineering using structured user inputs
- Clean and minimal Flask architecture
- Containerized deployment with CI/CD
