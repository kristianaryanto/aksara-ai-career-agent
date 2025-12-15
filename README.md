# Aksara Global: Intelligent AI Agent for Global Talent Upskilling 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20Framework-green)
![LLM](https://img.shields.io/badge/LLM-Gemini%201.5%20Flash-orange)
![Docker](https://img.shields.io/badge/Infrastructure-Docker%20Compose-blue)

> **An end-to-end Generative AI platform that performs automated Skill Gap Analysis and dynamic curriculum synthesis using Large Language Models (LLMs).**

---

## 📋 Project Overview

Aksara Global is designed to bridge the gap between local digital talent and global market demands. Unlike traditional platforms that offer static courses, this system utilizes **Agentic Reasoning** to analyze unstructured data (CVs and Job Descriptions) and generate a hyper-personalized learning trajectory.

### The Problem
Traditional e-learning is generic. Talents often possess skills that are "close but not enough" for global roles.

### The AI Solution
The system acts as a **Career Architect**, using **Google Gemini 1.5** to identify semantic gaps in technical expertise and automatically fetching real-world learning resources via the **YouTube Data API**.

---

## 🧠 AI & Data Engineering Features

### 1. Semantic Skill Gap Analysis (LLM Reasoning)
Instead of simple keyword matching, the engine performs deep semantic analysis of a candidate's profile.
* **Input Handling:** Extracts text from PDFs (CVs) using `PyPDF2`.
* **Reasoning Layer:** Utilizes Gemini 1.5 Flash to compare extracted skills against real-world job requirements.
* **Structured Output:** Implements rigorous **JSON Enforcement** in prompts to ensure LLM outputs are programmatically parsable for the frontend.

### 2. Dynamic Content Orchestration
The system doesn't just suggest topics; it populates them with live data.
* **Automated Query Generation:** The AI generates specific search queries for each skill gap identified.
* **Resource Integration:** Integration with **YouTube Data API v3** to fetch the most relevant, high-quality video tutorials for each specific module in the generated roadmap.

### 3. Modern Microservices Architecture
The project is built with scalability and production-readiness in mind:
* **Asynchronous Backend:** FastAPI for high-performance, non-blocking I/O operations.
* **Containerization:** Full Dockerization for both Backend and Frontend, ensuring "it works on my machine" everywhere.
* **Data Presentation:** A React-based dashboard that visualizes the AI's complex reasoning into a user-friendly roadmap.

---

## 🛠️ Tech Stack

| Domain | Technology |
| :--- | :--- |
| **AI/LLM** | Google Gemini 1.5 Flash API |
| **Backend** | Python, FastAPI, Pydantic (Data Validation) |
| **Frontend** | React.js, Vite, TailwindCSS |
| **Data Processing** | PyPDF2, BeautifulSoup4 (Scraping) |
| **External APIs** | YouTube Data API v3 |
| **DevOps** | Docker, Docker Compose |

---

## 📐 System Flow

1. **User Uploads Resume (PDF)** ➡️ Text Extraction.
2. **AI Analysis** ➡️ Gemini compares Resume vs. Target Job Role.
3. **Curriculum Synthesis** ➡️ AI determines duration (weeks) and specific technical modules.
4. **Resource Enrichment** ➡️ Backend fetches YouTube tutorials for every module.
5. **Final Output** ➡️ A full-stack interactive learning path for the user.

---

## 💻 Technical Implementation Highlights

### Prompt Engineering & JSON Extraction
The core value lies in the `gemini_service.py`, where the LLM is instructed to act as a career expert. The prompt engineering ensures a strict JSON structure:

```python
# Strategic Prompting Example
prompt = f"""
    Analyze the following resume and job target. 
    Identify missing technical skills and construct a week-by-week learning plan.
    RETURN ONLY A VALID JSON OBJECT with keys: 'summary', 'estimated_weeks', 'modules'.
"""

```

###Automated Web Scraping (Demo)The project includes a BeautifulSoup-based scraper designed to fetch job descriptions, demonstrating an understanding of data acquisition workflows.

---

##🚀 Future Roadmap* **RAG (Retrieval-Augmented Generation):** Implementing a Vector Database (ChromaDB/Pinecone) to store and retrieve curriculum templates.
* **Multi-Agent Workflow:** Using frameworks like CrewAI or LangGraph to separate the "Analyzer Agent" from the "Curriculum Architect Agent."
* **Skill Verification:** Integrating automated quizzes to validate progress within the roadmap.

