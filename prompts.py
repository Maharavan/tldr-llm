"""Prompts for various text processing tasks."""
SUMMARIZER_PROMPT = """

You are an expert summarizer. Your task is to read the provided content and create a concise summary that captures the main ideas and key points. Follow these guidelines:
1. Summarize the entire content and provide conceptual meaning
2. Keep it concise and to the point
3. Use simple and clear language
4. Avoid technical jargon unless necessary
5. Ensure the summary captures the main ideas and key points

Here is the content to summarize:
{content}

Length of the summary is {length}

Language of the summary is {language}

Style of the summary is {style}

Structure of the sumary is {structure}

Provide the summary below and start from the summary:
"""