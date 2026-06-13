import google.generativeai as genai

from config import GEMINI_API_KEY


class RepositoryAssistant:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def ask(self, report, question):

        prompt = f"""
You are a senior software architect.

Repository Analysis Report:

{report}

User Question:
{question}

Answer professionally as a software architect.
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text