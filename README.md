# AI Engineering Bootcamp - RAG Chatbot System

A full-stack Retrieval-Augmented Generation (RAG) chatbot system for product search and information retrieval, built with modern AI/ML technologies and containerized microservices architecture.

## Overview

This project implements an intelligent chatbot that answers questions about Amazon electronics products using semantic search and large language models. The system demonstrates:

- **Vector embeddings** and semantic search with Qdrant
- **RAG pipeline** implementation for grounded AI responses
- **Full-stack AI application** development (FastAPI + Streamlit)
- **Docker containerization** and microservices orchestration
- **Multi-provider LLM** integration (OpenAI, Google GenAI, Groq)

## Architecture

```
┌─────────────────────────────────────────────────┐
│         Streamlit Chatbot UI (Port 8501)        │
│         User-facing chat interface              │
└────────────────┬────────────────────────────────┘
                 │ HTTP/REST
                 ▼
┌─────────────────────────────────────────────────┐
│      FastAPI Backend/RAG Engine (Port 8000)     │
│  - RAG pipeline orchestration                   │
│  - LLM integration (OpenAI/Google/Groq)         │
│  - Vector store communication                   │
└────────────────┬────────────────────────────────┘
                 │ Vector Query
                 ▼
┌─────────────────────────────────────────────────┐
│    Qdrant Vector Database (Port 6333/6334)     │
│  - Amazon product embeddings storage            │
│  - Semantic similarity search                   │
└─────────────────────────────────────────────────┘
```

## Key Features

- **Semantic Search**: Uses OpenAI embeddings to find relevant products based on meaning, not keywords
- **Context-Grounded Answers**: LLM responses are based only on retrieved product data
- **Real-time Chat Interface**: Interactive Streamlit UI with conversation history
- **Error Handling**: Graceful degradation with user-friendly error messages
- **Request Tracking**: Unique request IDs for debugging and monitoring
- **Multi-Model Support**: Configurable LLM providers (OpenAI, Google, Groq)
- **Production-Ready**: Containerized with Docker, non-root users, structured logging

## Tech Stack

### Core Technologies
- **Python 3.12** - Runtime language
- **FastAPI 0.118+** - High-performance async API framework
- **Streamlit 1.50+** - Rapid UI development
- **Qdrant** - Vector database for semantic search
- **OpenAI API** - Embeddings (text-embedding-3-small) and generation (GPT-4 mini)
- **Docker & Docker Compose** - Container orchestration

### Key Dependencies
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server for FastAPI
- **uv** - Fast Python package manager
- **Jupyter** - Notebooks for experimentation
- **Pandas** - Data manipulation
- **Matplotlib** - Visualization

## Project Structure

```
01-ai-engineering-bootcamp/
├── src/
│   ├── api/                        # FastAPI backend
│   │   ├── app.py                  # Application entry point
│   │   ├── core/
│   │   │   └── config.py           # Configuration management
│   │   ├── api/
│   │   │   ├── endpoints.py        # API routes
│   │   │   ├── models.py           # Pydantic schemas
│   │   │   └── middleware.py       # Request tracking
│   │   └── rag/
│   │       └── retrieval_generation.py  # RAG pipeline
│   │
│   └── chatbot_ui/                 # Streamlit frontend
│       ├── app.py                  # Main UI application
│       └── core/
│           └── config.py           # UI configuration
│
├── notebooks/                      # Jupyter notebooks
│   ├── week_1/
│   │   ├── 01-llm-apis.ipynb      # LLM API exploration
│   │   ├── 02-explore-amazon-dataset.ipynb
│   │   └── 03-explore-arxiv-api.ipynb
│   └── week_2/
│       ├── 01-RAG-preprocessing-Amazon.ipynb
│       ├── 02-RAG-pipeline.ipynb
│       └── 03-Patrick-GPT-models.ipynb
│
├── data/                           # Dataset storage
│   ├── Electronics.jsonl           # Amazon electronics data
│   ├── meta_Electronics.jsonl      # Product metadata
│   └── Electornics_2022_2023_*     # Filtered datasets
│
├── qdrant_storage/                 # Vector DB persistent storage
├── docker-compose.yml              # Service orchestration
├── Dockerfile.fastapi              # Backend container
├── Dockerfile.streamlit            # Frontend container
├── pyproject.toml                  # Dependencies
├── .env.example                    # Environment template
└── Makefile                        # Build commands
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- API keys for:
  - OpenAI (required)
  - Google GenAI (optional)
  - Groq (optional)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yippa1205/01-ai-engineering-bootcamp.git
   cd 01-ai-engineering-bootcamp
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys:
   # OPENAI_API_KEY=your-key-here
   # GOOGLE_API_KEY=your-key-here (optional)
   # GROQ_API_KEY=your-key-here (optional)
   ```

3. **Start the application**
   ```bash
   make run-docker-compose
   # OR manually:
   docker compose up --build
   ```

4. **Access the chatbot**
   - Frontend UI: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Qdrant UI: http://localhost:6333/dashboard

## How It Works

### RAG Pipeline Flow

1. **User Query** → Streamlit captures user input
2. **API Request** → POST to `/rag/` endpoint with query
3. **Embedding** → Query converted to vector via OpenAI
4. **Retrieval** → Qdrant finds top-5 similar products
5. **Context Building** → Retrieved products formatted as context
6. **Prompt Engineering** → System prompt + context + query
7. **Generation** → GPT-4 mini generates grounded answer
8. **Response** → Answer displayed in chat interface

### Data Preparation

The Amazon electronics dataset is processed through Jupyter notebooks:

1. **Preprocessing** (`01-RAG-preprocessing-Amazon.ipynb`)
   - Filter by date range (2022-2023)
   - Sample datasets for testing
   - Clean and format data

2. **Pipeline Setup** (`02-RAG-pipeline.ipynb`)
   - Generate embeddings via OpenAI
   - Upload to Qdrant vector database
   - Create collection: "Amazon-items-collection-00"

## API Endpoints

### POST `/rag/`

Processes a user query through the RAG pipeline.

**Request:**
```json
{
  "query": "What laptops are available?"
}
```

**Response:**
```json
{
  "request_id": "uuid-here",
  "answer": "Based on available products, here are some laptops..."
}
```

## Development

### Local Development without Docker

```bash
# Install dependencies
uv sync

# Run backend (from project root)
cd src/api
uvicorn app:app --reload --port 8000

# Run frontend (separate terminal)
cd src/chatbot_ui
streamlit run app.py
```

### Running Notebooks

```bash
# Activate environment
source .venv/bin/activate

# Launch Jupyter
jupyter lab
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY` - Required for embeddings and generation
- `GOOGLE_API_KEY` - Optional alternative LLM
- `GROQ_API_KEY` - Optional fast inference API
- `API_URL` - Backend URL (default: http://api:8000)

### Docker Services

All services defined in `docker-compose.yml`:

- **streamlit-app**: Frontend on port 8501
- **api**: Backend on port 8000
- **qdrant**: Vector DB on ports 6333/6334

## Troubleshooting

### Common Issues

**KeyError: 'answer'**
- Ensure API container is running: `docker ps`
- Check API logs: `docker logs 01-ai-engineering-bootcamp-api-1`
- Restart API: `docker restart 01-ai-engineering-bootcamp-api-1`

**Connection refused**
- Verify all containers are running: `docker compose ps`
- Check docker network: `docker network inspect 01-ai-engineering-bootcamp_default`

**Empty Qdrant responses**
- Ensure data is loaded into Qdrant (run preprocessing notebook)
- Check Qdrant UI: http://localhost:6333/dashboard

## CI/CD

GitHub Actions workflows:
- `.github/workflows/code-review.yml` - Automated code review
- `.github/workflows/security-review.yml` - Security scanning
- `.github/workflows/claude.yml` - Claude AI integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper error handling
4. Ensure tests pass (if applicable)
5. Submit a pull request

## License

This project is part of an AI Engineering Bootcamp educational program.

## Acknowledgments

- Amazon Electronics dataset for training data
- OpenAI for embeddings and LLM APIs
- Qdrant for vector search capabilities
- FastAPI and Streamlit communities
