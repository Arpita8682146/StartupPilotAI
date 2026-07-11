# 🚀 StartupPilotAI

**Your AI Co-Founder for Startup Success**

StartupPilotAI is an AI-powered platform that helps entrepreneurs understand startup-related documents using Retrieval-Augmented Generation (RAG) and Google Gemini.

Upload startup guides, legal agreements, funding schemes, and business documents — then ask questions in natural language and get accurate, context-aware answers grounded in your own documents.

🔗 **Live app:** [startuppilotai.streamlit.app](https://startuppilotai.streamlit.app)

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#️-tech-stack)
- [Architecture](#️-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#️-getting-started)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Roadmap](#️-roadmap)
- [Development Log](#-development-log)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Problem Statement

Entrepreneurs often struggle to understand startup policies, funding opportunities, legal documents, and compliance requirements because information is scattered across multiple lengthy documents.

StartupPilotAI solves this by letting users upload documents and receive intelligent, document-grounded answers — instead of manually digging through hundreds of pages.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 PDF Upload | Upload startup-related documents directly into the platform |
| 🤖 AI Question Answering | Ask natural-language questions based on uploaded documents |
| 🔍 Cited Answers | Every answer links back to the exact source document, page, and similarity score |
| 💬 Conversational Chat | Multi-turn chat with history-aware context for follow-up questions |
| 📝 Document Summarization | Generate concise summaries of long documents |
| ⚖️ Legal Language Simplifier | Explain complex legal clauses and contract terms in plain language |
| 📊 Startup Readiness Assessment | Evaluate how prepared your startup is with an automated readiness score |
| 💰 Funding Recommendation | Get funding scheme suggestions matched to your stage, industry, and target amount |
| 🗺️ Personalized Roadmap | Generate a milestone-based launch roadmap from your goals and documents |
| 📈 Analytics Dashboard | Visualize indexed documents, chunk counts, and word-count stats |
| 🔐 Bring Your Own API Key | Optionally supply your own Gemini API key from the sidebar |
| ☁️ Cloud Deployed | Live and publicly accessible via Streamlit Community Cloud |

---

## 🖼️ Demo

🔗 Try it live: **[startuppilotai.streamlit.app](https://startuppilotai.streamlit.app)**

*Screenshots coming soon — `assets/screenshots/`*

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI Framework | Streamlit |
| LLM | Google Gemini |
| Vector Database | ChromaDB |
| Embeddings | Google Gemini Embedding API |
| PDF Parsing | PyMuPDF |
| Containerization | Docker |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

## 🏗️ Architecture

```
                          User
                           │
                           ▼
              Streamlit Interface
        Upload • Search • Ask • Analyze
                           │
                           ▼
                StartupPilotAI Engine
                           │
          ┌────────────────┴────────────────┐
          │                                  │
          ▼                                  ▼
  Document Processing               Query Processing
      PDF Upload                       User Query
          │                                  │
          ▼                                  ▼
       PyMuPDF                     Semantic Search
          │                                  │
          ▼                                  ▼
      Chunking                    ChromaDB Retrieval
          │                                  │
          ▼                                  ▼
     Embeddings                   Relevant Context
          │                                  │
          └────────────────┬─────────────────┘
                            ▼
                     Prompt Builder
                            │
                            ▼
                     Google Gemini
                            │
                            ▼
             AI Startup Recommendations
       Funding • Legal • Compliance • Registration
                    Personalized Roadmaps
```

The full architecture write-up lives in `docs/rag_architecture.md`.

---

## 📁 Project Structure

```
StartupPilotAI/
│
├── Dockerfile                 # Container build definition
├── .dockerignore
├── requirements.txt           # Python dependencies
├── README.md
├── LICENSE
├── .gitignore
├── .env                       # Local secrets (not committed)
│
├── docs/
│   ├── rag_architecture.md    # Detailed RAG architecture notes
│   └── data/
│       └── src/
│           ├── app.py             # Streamlit entry point
│           ├── pdf_loader.py      # PDF text extraction (PyMuPDF)
│           ├── chunking.py        # Semantic document chunking
│           ├── embeddings.py      # Embedding generation (Gemini API)
│           ├── vectorstore.py     # ChromaDB integration
│           ├── retriever.py       # Semantic search & retrieval
│           ├── gemini_client.py   # Google Gemini API client
│           ├── advisor.py         # Readiness, funding, roadmap, legal tools
│           └── prompt_builder.py  # RAG prompt construction
│
├── chroma_db/                 # Persisted vector embeddings
│
└── venv/                      # Virtual environment (not committed)
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API key
- Docker (optional, for containerized deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/StartupPilotAI.git
cd StartupPilotAI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### Run the app

```bash
streamlit run docs/data/src/app.py
```

The app will be available at `http://localhost:8501`.

---

## 🚀 Usage

1. Launch the app with `streamlit run docs/data/src/app.py` (or visit the [live app](https://startuppilotai.streamlit.app)).
2. Upload one or more startup-related PDF documents from the sidebar.
3. Wait for the document to be processed, chunked, and embedded.
4. Ask questions in natural language, e.g.:
   - "What funding schemes am I eligible for?"
   - "Summarize the compliance requirements in this document."
   - "Explain clause 4.2 in simple terms."
5. Review AI-generated summaries, readiness scores, funding matches, and roadmap suggestions across the three tabs.

---

## 🌐 Deployment

The app is live on **Streamlit Community Cloud**: [startuppilotai.streamlit.app](https://startuppilotai.streamlit.app)

It is also containerized with Docker for portable deployment elsewhere:

```bash
# Build the image
docker build -t startuppilotai .

# Run locally
docker run -p 8501:8501 --env-file .env startuppilotai
```

The image can also be pushed to a container registry (e.g. Docker Hub) and deployed to any platform that accepts a container, such as Render, Koyeb, or Google Cloud Run. The app originally relied on a local `sentence-transformers` model for embeddings, which pushed memory usage past the 512MB limit on several free-tier hosts. Switching to the Gemini Embedding API removed that local model dependency entirely and significantly reduced the app's runtime memory footprint.

---

## 🗺️ Roadmap

- [ ] Multi-document cross-referencing
- [ ] Support for DOCX and scanned/OCR PDFs
- [ ] User authentication and saved sessions
- [ ] Export reports (readiness score, roadmap) as PDF
- [ ] Persistent volume for vector store data in production

---

## 📅 Development Log

### Week 1

| Day | Progress |
|---|---|
| Day 1 | Implemented PDF loading pipeline using PyMuPDF |
| Day 2 | Built a document chunking module for semantic splitting |
| Day 3 | Generated embeddings using Sentence Transformers |
| Day 4 | Integrated ChromaDB for vector storage |
| Day 5 | Implemented semantic similarity search |
| Day 6 | Developed context retrieval functionality |
| Day 7 | Created a prompt builder for RAG prompts |

### Week 2

| Day | Progress |
|---|---|
| Day 8 | Fixed a circular import between `gemini_client.py` and `retriever.py`; removed a hardcoded API key in favor of environment-variable configuration |
| Day 9 | Cleaned up duplicate `app.py` copies and stray `__pycache__` files; resolved git merge/rebase conflicts and consolidated the project into a single source tree |
| Day 10 | Set up Docker: wrote a `Dockerfile` and `.dockerignore`, and containerized the Streamlit app |
| Day 11 | Built and pushed the Docker image to Docker Hub for portable deployment |
| Day 12 | Deployed to Render; diagnosed and resolved a reverse-proxy connection issue behind the platform's load balancer |
| Day 13 | Diagnosed an out-of-memory crash on free-tier hosting (512MB RAM limit) caused by the local `sentence-transformers`/`torch` stack; migrated embedding generation to the Gemini Embedding API to cut the app's memory footprint |
| Day 14 | Evaluated deployment alternatives (Koyeb, Google Cloud Run, Streamlit Community Cloud, Snowflake); deployed successfully to **Streamlit Community Cloud**, now live at [startuppilotai.streamlit.app](https://startuppilotai.streamlit.app) |

*Week 3 log to be added.*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
