# Claude Code Configuration

## Project Overview
This is an AI Engineering Bootcamp repository featuring:
- **FastAPI Backend** (`src/api`) - REST API for AI services
- **Chatbot UI** (`src/chatbot_ui`) - Streamlit-based chat interface
- **Jupyter Notebooks** (`notebooks`) - Learning materials and experiments
- **Qdrant Vector DB** - Vector storage for embeddings
- **Docker Setup** - Containerized deployment

## Code Style Guidelines

### Python
- Use Python 3.12+ with type hints
- Follow PEP 8 style guide
- Format code with Black (line length: 88)
- Use meaningful, descriptive variable and function names
- Prefer async/await for I/O operations

### File Organization
- Use 2-space indentation for YAML and JSON
- Use 4-space indentation for Python
- Keep imports organized: standard library, third-party, local
- One class per file for major components

## Project Structure

```
├── src/
│   ├── api/              # FastAPI backend
│   │   ├── api/         # API endpoints, models, middleware
│   │   └── core/        # Configuration
│   └── chatbot_ui/      # Streamlit frontend
│       ├── app.py       # Main application
│       └── core/        # Configuration
├── notebooks/           # Jupyter notebooks for learning
├── data/               # Data files and datasets
├── qdrant_storage/     # Vector database storage
└── docker-compose.yml  # Container orchestration
```

## Review Criteria

### Code Quality
- All new functions must include type hints
- Docstrings required for public functions and classes
- Error handling with try/except for external operations
- No hardcoded credentials (use environment variables)

### Security
- Validate all user inputs
- Check for SQL injection vulnerabilities
- Verify API key storage uses environment variables
- Scan for exposed secrets in code
- Review dependencies for known vulnerabilities

### Testing
- Unit tests for business logic
- Integration tests for API endpoints
- Test error handling paths
- Verify edge cases

### AI/ML Specific
- Document model versions and parameters
- Include data validation for embeddings
- Verify vector database connections
- Check API rate limits and timeouts
- Monitor token usage for LLM calls

## Preferred Patterns

### FastAPI Backend
```python
# Use dependency injection
from fastapi import Depends, FastAPI
from typing import Annotated

async def get_current_user(token: str) -> User:
    # Validate token
    return user

@app.get("/api/endpoint")
async def endpoint(user: Annotated[User, Depends(get_current_user)]):
    # Use the dependency
    pass
```

### Error Handling
```python
from fastapi import HTTPException

try:
    result = await external_api_call()
except APIError as e:
    raise HTTPException(status_code=503, detail=str(e))
```

### Environment Variables
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    database_url: str

    class Config:
        env_file = ".env"
```

### Async Operations
```python
# Prefer async for I/O
async def fetch_embeddings(text: str) -> list[float]:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={"text": text})
        return response.json()["embeddings"]
```

## Merge Checklist

- [ ] All tests pass locally
- [ ] Code follows style guidelines
- [ ] Type hints added for new functions
- [ ] Documentation updated (if API changes)
- [ ] No security vulnerabilities introduced
- [ ] Environment variables used for secrets
- [ ] Error handling implemented
- [ ] Backward compatibility maintained (or documented)
- [ ] Dependencies updated in pyproject.toml
- [ ] Docker builds successfully (if infrastructure changed)

## Common Issues to Watch For

### Performance
- Avoid synchronous I/O in async functions
- Use connection pooling for databases
- Implement caching for expensive operations
- Monitor vector database query performance

### Security
- Never commit `.env` files
- Validate file uploads (size, type)
- Sanitize inputs before database queries
- Use HTTPS in production
- Implement rate limiting on APIs

### AI/ML Specific
- Handle LLM API timeouts gracefully
- Implement retry logic with exponential backoff
- Validate embedding dimensions match expectations
- Monitor token costs and usage limits
- Cache embeddings when possible

## Development Workflow

1. **Create feature branch** from main
2. **Write code** following style guidelines
3. **Add tests** for new functionality
4. **Run tests locally** and verify they pass
5. **Create Pull Request** with clear description
6. **Address review feedback** from Claude or team
7. **Merge** after approval

## Useful Commands

```bash
# Run FastAPI backend
uvicorn src.api.app:app --reload

# Run Streamlit UI
streamlit run src/chatbot_ui/app.py

# Run with Docker
docker-compose up

# Format code
black src/

# Type checking
mypy src/

# Run tests
pytest
```

## Learning Goals

This bootcamp focuses on:
- Building production-ready AI applications
- API design and implementation
- Vector databases and embeddings
- LLM integration patterns
- Containerization and deployment
- Security best practices

## Questions to Ask During Review

1. Does this code introduce security vulnerabilities?
2. Are there opportunities to improve performance?
3. Is error handling comprehensive?
4. Are API responses properly typed?
5. Does this follow the project's architectural patterns?
6. Are there potential race conditions or async issues?
7. Is the code testable and maintainable?

---

*This file guides Claude Code in understanding your project's conventions and standards. Update it as your project evolves!*
