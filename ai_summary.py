"""Groq API helper for inventory summaries (triggers S.A.G.E. credential prompt)."""

import os


GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"


def get_groq_api_key():
    """Read the required GROQ_API_KEY from the environment."""
    return os.environ["GROQ_API_KEY"]


def build_auth_headers():
    """Return HTTP headers with Bearer authentication for Groq."""
    api_key = get_groq_api_key()
    return {
        "Authorization": api_key,
        "Content-Type": "application/json",
    }
