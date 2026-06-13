from backend.ai.repository_assistant import (
    RepositoryAssistant
)


class RepositoryChat:

    def __init__(self):

        self.assistant = RepositoryAssistant()

    def ask_question(
        self,
        report,
        question
    ):

        return self.assistant.ask(
            report,
            question
        )