from backend.analysis.architecture_drift import (
    ArchitectureDriftAnalyzer
)
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.utils.github_cloner import GitHubCloner
from backend.graph.repository_loader import RepositoryLoader
from backend.analysis.architecture_report import (
    ArchitectureReportGenerator
)
from backend.ai.repository_assistant import (
    RepositoryAssistant
)
from backend.reporting.pdf_report import (
    PDFReportGenerator
)
from backend.analysis.pr_risk_analyzer import (
    PullRequestRiskAnalyzer
)

app = FastAPI(
    title="Engineering Intelligence Platform"
)


class AnalyzeRequest(BaseModel):
    repo_url: str


class ChatRequest(BaseModel):
    repo_url: str
    question: str


class PRRequest(BaseModel):
    files: list

class DriftRequest(BaseModel):

    repo_url: str

    branch_1: str

    branch_2: str

@app.get("/")
def home():

    return {
        "message":
        "Engineering Intelligence Platform API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_repository(
    request: AnalyzeRequest
):

    cloner = GitHubCloner()

    repo_path = cloner.clone_repository(
        request.repo_url
    )

    loader = RepositoryLoader(
        "bolt://localhost:7687",
        "neo4j",
        "Ynvdeepak@24"
    )

    graph = loader.load_repository(
        repo_path
    )

    report_generator = (
        ArchitectureReportGenerator()
    )

    report = report_generator.generate(
        graph
    )

    return report


@app.post("/chat")
def chat_repository(
    request: ChatRequest
):

    cloner = GitHubCloner()

    repo_path = cloner.clone_repository(
        request.repo_url
    )

    loader = RepositoryLoader(
        "bolt://localhost:7687",
        "neo4j",
        "Ynvdeepak@24"
    )

    graph = loader.load_repository(
        repo_path
    )

    report_generator = (
        ArchitectureReportGenerator()
    )

    report = report_generator.generate(
        graph
    )

    assistant = RepositoryAssistant()

    answer = assistant.ask(
        report,
        request.question
    )

    return {
        "question":
        request.question,

        "answer":
        answer
    }


@app.post("/pr-risk")
def analyze_pr(
    request: PRRequest
):

    analyzer = (
        PullRequestRiskAnalyzer()
    )

    result = analyzer.analyze(
        request.files,
        [
            ("Flask", 19),
            ("Response", 7),
            ("Blueprint", 4),
            ("_CollectErrors", 3)
        ]
    )

    return result

@app.post("/architecture-drift")
def architecture_drift(
    request: DriftRequest
):

    cloner = GitHubCloner()

    repo_1 = (
        cloner.clone_branch(
            request.repo_url,
            request.branch_1
        )
    )

    repo_2 = (
        cloner.clone_branch(
            request.repo_url,
            request.branch_2
        )
    )

    loader = RepositoryLoader(
        "bolt://localhost:7687",
        "neo4j",
        "Ynvdeepak@24"
    )

    graph_1 = (
        loader.load_repository(
            repo_1
        )
    )

    graph_2 = (
        loader.load_repository(
            repo_2
        )
    )

    report_generator = (
        ArchitectureReportGenerator()
    )

    report_1 = (
        report_generator.generate(
            graph_1
        )
    )

    report_2 = (
        report_generator.generate(
            graph_2
        )
    )

    drift_analyzer = (
        ArchitectureDriftAnalyzer()
    )

    drift_report = (
        drift_analyzer.compare(
            report_1,
            report_2
        )
    )

    return drift_report
@app.get("/report")
def download_report():

    sample_report = {

        "project":
        "Engineering Intelligence Platform",

        "architecture_score":
        90,

        "technical_debt":
        "Medium",

        "risk_score":
        20
    }

    generator = (
        PDFReportGenerator()
    )

    file_name = (
        "architecture_report.pdf"
    )

    generator.generate(
        sample_report,
        file_name
    )

    return FileResponse(
        path=file_name,
        media_type="application/pdf",
        filename=file_name
    )
