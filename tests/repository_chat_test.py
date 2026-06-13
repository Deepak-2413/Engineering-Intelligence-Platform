from backend.ai.repository_chat import (
    RepositoryChat
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

chat = RepositoryChat()

while True:

    question = input(
        "\nAsk a repository question (or quit): "
    )

    if question.lower() == "quit":
        break

    answer = chat.ask_question(
        report,
        question
    )

    print("\n")
    print(answer)