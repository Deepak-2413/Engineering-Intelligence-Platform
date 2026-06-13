
import streamlit as st
import requests
import pandas as pd

from graph_view import show_graph

st.set_page_config(
    page_title="Engineering Intelligence Platform",
    layout="wide"
)

st.title(
    "Engineering Intelligence Platform"
)

repo_url = st.text_input(
    "GitHub Repository URL",
    "https://github.com/pallets/flask.git"
)

if "analysis_data" not in st.session_state:
    st.session_state.analysis_data = None

# =========================
# Repository Analysis
# =========================

if st.button(
    "Analyze Repository"
):

    with st.spinner(
        "Analyzing repository..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "repo_url": repo_url
            }
        )

        if response.status_code == 200:

            st.session_state.analysis_data = (
                response.json()
            )

        else:

            st.error(
                response.text
            )

data = st.session_state.analysis_data

# =========================
# Analysis Results
# =========================

if data:

    architecture_score = max(
        0,
        100 - data["risk_score"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Architecture Score",
        architecture_score
    )

    col2.metric(
        "Risk Score",
        data["risk_score"]
    )

    col3.metric(
        "Technical Debt (Hours)",
        data.get(
            "technical_debt_hours",
            0
        )
    )

    st.subheader(
        "Critical Components"
    )

    critical = pd.DataFrame(
        data["critical_components"],
        columns=[
            "Component",
            "Impact"
        ]
    )

    st.dataframe(
        critical,
        use_container_width=True
    )

    st.subheader(
        "Architecture Smells"
    )

    smells = data.get(
        "architecture_smells",
        []
    )

    if smells:

        for smell in smells:

            if isinstance(
                smell,
                dict
            ):

                st.warning(
                    f"{smell['type']} | "
                    f"{smell['component']} | "
                    f"{smell['details']}"
                )

            else:

                st.warning(
                    str(smell)
                )

    else:

        st.success(
            "No architecture smells detected"
        )

    # =========================
    # AI Recommendations
    # =========================

    st.subheader(
        "AI Refactoring Recommendations"
    )

    recommendations = data.get(
        "refactoring_recommendations",
        []
    )

    if recommendations:

        for recommendation in recommendations:

            st.info(
                f"""
Priority: {recommendation['priority']}

Action: {recommendation['action']}

Benefit: {recommendation['benefit']}
"""
            )

    else:

        st.success(
            "No recommendations generated"
        )

    # =========================
    # Dependency Overview
    # =========================

    st.subheader(
        "Dependency Overview"
    )

    st.write(
        f"Components: {data['components']}"
    )

    st.write(
        f"Dependencies: {data['dependencies']}"
    )

    st.write(
        f"Coupling: {data['coupling']}"
    )

    st.write(
        f"Health: {data['health']}"
    )

    st.write(
        f"Architecture Grade: "
        f"{data['architecture_grade']}"
    )

    st.write(
        f"Technical Debt Level: "
        f"{data['technical_debt_level']}"
    )

    # =========================
    # Security Findings
    # =========================

    st.subheader(
        "Security Findings"
    )

    findings = data.get(
        "security_findings",
        []
    )

    if findings:

        for finding in findings:

            st.error(
                str(finding)
            )

    else:

        st.success(
            "No security findings"
        )

    # =========================
    # Refactoring Roadmap
    # =========================

    st.subheader(
        "Refactoring Roadmap"
    )

    roadmap = data.get(
        "refactoring_roadmap",
        []
    )

    for step in roadmap:

        st.success(
            f"P{step['priority']} : "
            f"{step['action']}"
        )

    # =========================
    # Dependency Graph
    # =========================

    st.subheader(
        "Dependency Graph"
    )

    show_graph(
        data["dependency_graph"],
        data["critical_components"]
    )

# =========================
# Repository Chat Assistant
# =========================

st.divider()

st.subheader(
    "Repository Chat Assistant"
)

question = st.text_input(
    "Ask a question about the repository",
    "What should I refactor first?"
)

if st.button(
    "Ask AI"
):

    with st.spinner(
        "Thinking..."
    ):

        chat_response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "repo_url": repo_url,
                "question": question
            }
        )

        if chat_response.status_code == 200:

            answer = (
                chat_response.json()
            )

            st.success(
                answer["answer"]
            )

        else:

            st.error(
                chat_response.text
            )

# =========================
# Pull Request Risk Analyzer
# =========================

st.divider()

st.subheader(
    "Pull Request Risk Analyzer"
)

changed_files = st.text_area(
    "Changed Files (one per line)",
    """Flask/app.py
Config/settings.py
security/auth.py"""
)

if st.button(
    "Analyze PR Risk"
):

    files = [
        file.strip()
        for file in changed_files.split("\n")
        if file.strip()
    ]

    pr_response = requests.post(
        "http://127.0.0.1:8000/pr-risk",
        json={
            "files": files
        }
    )

    if pr_response.status_code == 200:

        result = (
            pr_response.json()
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "PR Risk Score",
            result["risk_score"]
        )

        col2.metric(
            "Risk Level",
            result["risk_level"]
        )

        st.subheader(
            "Risk Reasons"
        )

        for reason in result["reasons"]:

            st.warning(
                reason
            )

    else:

        st.error(
            pr_response.text
        )
# =========================

# Architecture Drift Analyzer

# =========================

st.divider()

st.subheader(
"Architecture Drift Analyzer"
)

branch_1 = st.text_input(
"Branch 1",
"main"
)

branch_2 = st.text_input(
"Branch 2",
"main"
)

if st.button(
"Compare Architectures"
):


    with st.spinner(
        "Comparing branches..."
    ):

        drift_response = requests.post(
            "http://127.0.0.1:8000/architecture-drift",
            json={
                "repo_url": repo_url,
                "branch_1": branch_1,
                "branch_2": branch_2
            }
        )

        if drift_response.status_code == 200:

            result = drift_response.json()

            st.subheader(
                "Drift Results"
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Architecture Score Change",
                result["score_change"]
            )

            col2.metric(
                "Risk Change",
                result["risk_change"]
            )

            col3, col4 = st.columns(2)

            col3.metric(
                "Debt Change",
                result["debt_change"]
            )

            col4.metric(
                "Smell Change",
                result["smell_change"]
            )

            status = result["status"]

            if status == "Improved":

                st.success(
                    f"Status: {status}"
                )

            elif status == "Stable":

                st.info(
                    f"Status: {status}"
                )

            else:

                st.error(
                    f"Status: {status}"
                )

        else:

            st.error(
                drift_response.text
            )

