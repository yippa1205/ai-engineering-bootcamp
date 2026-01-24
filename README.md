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
- **LLM Observability**: LangSmith integration for tracing and monitoring RAG pipeline
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
- **LangSmith** - Observability and tracing for LLM applications
- **LangGraph** - Graph-based workflow orchestration
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
3. **Embedding** → Query converted to vector via OpenAI (traced with LangSmith)
4. **Retrieval** → Qdrant finds top-5 similar products (traced with LangSmith)
5. **Context Building** → Retrieved products formatted as context (traced with LangSmith)
6. **Prompt Engineering** → System prompt + context + query (traced with LangSmith)
7. **Generation** → GPT-4 mini generates grounded answer (traced with LangSmith)
8. **Response** → Answer displayed in chat interface

All pipeline steps are instrumented with LangSmith's `@traceable` decorator for end-to-end observability, enabling performance monitoring, debugging, and optimization of the RAG workflow.

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

**Note:** The RAG pipeline now returns enhanced data including retrieved context IDs, full context documents, and similarity scores, though only the answer is exposed through the API endpoint. This enables better debugging and future enhancements.

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

## LangSmith Observability

The RAG pipeline is fully instrumented with LangSmith for comprehensive tracing and monitoring. Every function in the pipeline ([retrieval_generation.py](src/api/rag/retrieval_generation.py)) uses the `@traceable` decorator with enhanced metadata:

- `get_embedding()` - Tracks embedding API calls with token usage metadata
  - Custom naming: "embed_query"
  - Run type: "embedding"
  - Metadata: provider, model name, input/total tokens
- `retrieval_data()` - Monitors vector search performance and retrieval quality
  - Custom naming: "retrieve_data"
  - Run type: "retriever"
- `process_context()` - Traces context formatting steps
  - Custom naming: "format_retrieved_context"
  - Run type: "prompt"
- `build_prompt()` - Captures prompt engineering patterns
  - Custom naming: "build_prompt"
  - Run type: "prompt"
- `generate_answer()` - Tracks LLM generation with detailed usage metadata
  - Custom naming: "generate_answer"
  - Run type: "llm"
  - Metadata: provider, model name, input/output/total tokens
- `rag_pipeline()` - End-to-end pipeline observability with enriched response
  - Custom naming: "rag_pipeline"
  - Returns comprehensive result including context, scores, and answer

### Enhanced Features

- **Token Usage Tracking**: Automatic capture of input, output, and total tokens for embedding and LLM calls
- **Custom Run Names**: Meaningful names for each trace step in LangSmith dashboard
- **Type Classification**: Proper categorization (embedding, retriever, prompt, llm) for better filtering
- **Provider Metadata**: Track which AI provider and model is used for each operation
- **Rich Response Data**: Pipeline now returns full context including retrieved IDs, documents, and similarity scores

### Benefits

- **Performance Monitoring**: Track latency at each pipeline step with detailed breakdowns
- **Cost Tracking**: Monitor API token usage and costs with precise per-call metrics
- **Debugging**: Inspect inputs/outputs at each stage with enhanced metadata
- **Quality Analysis**: Evaluate retrieval relevance and answer quality with similarity scores
- **Optimization**: Identify bottlenecks and improvement opportunities using categorized traces

### Setup LangSmith (Optional)

1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Get your API key from project settings
3. Add to `.env`:
   ```bash
   LANGSMITH_API_KEY=your-langsmith-key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_PROJECT=rag-chatbot
   ```
4. Restart the application to enable tracing
5. View traces in the LangSmith dashboard

## Configuration

### Environment Variables

- `OPENAI_API_KEY` - Required for embeddings and generation
- `GOOGLE_API_KEY` - Optional alternative LLM
- `GROQ_API_KEY` - Optional fast inference API
- `LANGSMITH_API_KEY` - Optional for LangSmith tracing and monitoring
- `LANGCHAIN_TRACING_V2` - Set to "true" to enable LangSmith tracing
- `LANGCHAIN_PROJECT` - Project name for organizing traces in LangSmith
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
