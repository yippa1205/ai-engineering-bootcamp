---
description: Perform a comprehensive code review of the pull request
---

# Code Review

Please perform a thorough code review of this pull request. Follow the guidelines in CLAUDE.md and focus on:

## Code Quality
- **Code Style**: Does the code follow PEP 8 and project conventions?
- **Type Hints**: Are type hints present and correct for all functions?
- **Naming**: Are variables, functions, and classes named clearly and descriptively?
- **Documentation**: Are docstrings present for public functions and classes?
- **Complexity**: Is the code simple and maintainable, or overly complex?

## Functionality
- **Correctness**: Does the code do what it's supposed to do?
- **Edge Cases**: Are edge cases and error conditions handled properly?
- **Error Handling**: Are exceptions caught and handled appropriately?
- **Async/Await**: Are async operations used correctly for I/O?

## AI/ML Specific (if applicable)
- **API Integration**: Are LLM API calls implemented with proper error handling?
- **Token Management**: Is there monitoring or limiting of token usage?
- **Vector Operations**: Are embeddings and vector operations handled correctly?
- **Data Validation**: Is input data validated before processing?
- **Timeouts**: Are appropriate timeouts set for external API calls?

## Architecture & Patterns
- **Separation of Concerns**: Is code properly organized and modular?
- **Dependencies**: Are dependencies injected properly (FastAPI Depends)?
- **Configuration**: Are settings managed through environment variables?
- **Database**: Are database connections and queries handled efficiently?

## Testing
- **Test Coverage**: Are there tests for new functionality?
- **Test Quality**: Do tests cover edge cases and error paths?

## Performance
- **Efficiency**: Are there obvious performance issues?
- **Caching**: Could caching improve performance?
- **Database Queries**: Are queries optimized (e.g., N+1 issues)?

## Security (Quick Check)
- **Input Validation**: Is user input validated and sanitized?
- **Secrets**: Are there any hardcoded credentials or API keys?
- **Dependencies**: Are new dependencies from trusted sources?

---

## Review Format

Please provide your review as:

1. **Summary**: Brief overview of the changes
2. **Strengths**: What's done well
3. **Issues**: Problems that should be fixed before merging
4. **Suggestions**: Optional improvements
5. **Verdict**: Approve, Request Changes, or Comment

Be constructive and specific. Reference file paths and line numbers when pointing out issues.
