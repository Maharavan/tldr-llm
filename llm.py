"""Module for interacting with the Groq LLM model to summarize text."""
import os
from groq import Groq
from dotenv import load_dotenv
from prompts import SUMMARIZER_PROMPT


load_dotenv()
def summarize_text(text: str) -> str:
    """Summarizes the given text using a Groq LLM model."""
    groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role":"user",
            "content": SUMMARIZER_PROMPT.format(content=text)
        }],
        temperature = 0.5
    )
    return completion.choices[0].message.content