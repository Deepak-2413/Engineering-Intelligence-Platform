\# Engineering Intelligence Platform (EIP)



\## Overview



Engineering Intelligence Platform (EIP) is an AI-powered software architecture analysis platform that helps engineers understand, evaluate, and improve large codebases. The platform automatically analyzes GitHub repositories, constructs dependency knowledge graphs, detects architectural issues, evaluates repository health, identifies pull request risks, and provides AI-driven engineering insights.



Built using FastAPI, Neo4j, Streamlit, and Gemini AI, EIP transforms repository data into actionable architecture intelligence for developers and engineering teams.



\---



\## Key Features



\### Repository Architecture Analysis



\* Clone and analyze GitHub repositories automatically

\* Build dependency knowledge graphs

\* Calculate architecture health metrics

\* Identify critical system components



\### Architecture Drift Analyzer



\* Compare repository architectures across branches

\* Detect architecture degradation or improvements

\* Measure changes in risk, technical debt, and architecture quality

\* Generate drift reports



\### Pull Request Risk Analyzer



\* Evaluate change impact before merging

\* Calculate risk scores for modified files

\* Highlight high-risk components

\* Provide risk-level classifications



\### AI Engineering Assistant



\* Ask natural language questions about repositories

\* Receive AI-generated engineering insights

\* Get architecture recommendations and refactoring guidance



\### Dependency Graph Visualization



\* Interactive visualization of repository structure

\* Dependency relationship mapping

\* Critical component highlighting



\### PDF Report Generation



\* Export architecture analysis reports

\* Generate shareable engineering documentation



\### Security \& Quality Insights



\* Detect architecture smells

\* Evaluate repository health

\* Track technical debt indicators

\* Identify maintainability concerns



\---



\## Technology Stack



\### Backend



\* Python

\* FastAPI

\* Neo4j

\* GitPython



\### AI Layer



\* Google Gemini API



\### Frontend



\* Streamlit



\### Data \& Visualization



\* NetworkX

\* Streamlit-Agraph



\---



\## System Architecture



GitHub Repository

↓

Repository Cloner

↓

Dependency Analyzer

↓

Neo4j Knowledge Graph

↓

Architecture Intelligence Engine

↓

AI Recommendation Layer

↓

Interactive Dashboard



\---



\## Project Modules



\* Repository Analysis Engine

\* Knowledge Graph Generator

\* Architecture Report Generator

\* Pull Request Risk Analyzer

\* Architecture Drift Analyzer

\* AI Repository Assistant

\* PDF Reporting Engine

\* Interactive Dashboard



\---



\## Getting Started



\### Clone Repository



```bash

git clone https://github.com/Deepak-2413/Engineering-Intelligence-Platform.git

cd Engineering-Intelligence-Platform

```



\### Create Virtual Environment



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Run Backend



```bash

uvicorn backend.api.app:app --reload

```



\### Run Dashboard



```bash

streamlit run dashboard/app.py

```



\---



\## Future Enhancements



\* Multi-repository comparison

\* CI/CD integration

\* Automated architecture governance

\* Advanced security scanning

\* Team collaboration dashboard

\* Historical architecture trend analysis



\---



\## Author



Yadlapalli Naga Venkata Deepak



Engineering Intelligence Platform — AI-Powered Software Architecture Intelligence



