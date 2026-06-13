
from backend.ai.repository_assistant import (
    RepositoryAssistant
)

report = """
Components: 52
Dependencies: 312
Health: Complex

Most Connected Component:
Flask

Critical Components:
_CollectErrors
ScriptInfo
EnvironBuilder

Cycle Found:
False
"""

assistant = RepositoryAssistant()

response = assistant.ask(
    report,
    "Summarize this repository architecture and identify risks."
)

print("\nAI RESPONSE\n")
print(response)