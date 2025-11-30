---
description: Perform a comprehensive security review of the pull request
---

# Security Review

Please perform a thorough security review of this pull request. Focus on identifying vulnerabilities and security risks:

## OWASP Top 10 Checks

### 1. Injection Vulnerabilities
- **SQL Injection**: Are database queries parameterized? Any string concatenation in queries?
- **Command Injection**: Are system commands constructed safely? Any use of `os.system()`, `subprocess.call()` with user input?
- **LDAP/NoSQL Injection**: Are queries to non-relational databases properly sanitized?
- **Prompt Injection**: For LLM interactions, is user input properly validated to prevent prompt manipulation?

### 2. Broken Authentication
- **Password Storage**: Are passwords hashed with strong algorithms (bcrypt, argon2)?
- **Session Management**: Are sessions handled securely? Proper timeout?
- **Token Security**: Are JWT tokens validated properly? Appropriate expiration?
- **Multi-factor Authentication**: Is MFA implemented where needed?

### 3. Sensitive Data Exposure
- **Credentials in Code**: Are there any hardcoded passwords, API keys, or secrets?
- **Logging**: Are sensitive data (passwords, tokens, PII) excluded from logs?
- **Error Messages**: Do error messages reveal sensitive information?
- **Environment Variables**: Are secrets properly loaded from `.env` and not committed?

### 4. XML External Entities (XXE)
- **XML Parsing**: If XML is parsed, are external entities disabled?
- **File Upload**: Are uploaded files validated properly?

### 5. Broken Access Control
- **Authorization**: Are authorization checks present for protected resources?
- **IDOR**: Can users access resources by changing IDs in URLs?
- **Privilege Escalation**: Can regular users access admin functions?
- **CORS**: Are CORS policies properly configured?

### 6. Security Misconfiguration
- **Debug Mode**: Is debug mode disabled in production?
- **Default Credentials**: Are default passwords changed?
- **Unnecessary Features**: Are unused features/endpoints disabled?
- **Security Headers**: Are appropriate security headers set (HSTS, CSP, etc.)?

### 7. Cross-Site Scripting (XSS)
- **Input Sanitization**: Is user input escaped/sanitized before rendering?
- **Content-Type Headers**: Are proper content-type headers set?
- **DOM Manipulation**: Is DOM manipulation safe from XSS?

### 8. Insecure Deserialization
- **Pickle/YAML**: Are `pickle.loads()` or `yaml.load()` used with untrusted data?
- **JSON Parsing**: Is JSON parsing safe from prototype pollution?

### 9. Using Components with Known Vulnerabilities
- **Dependencies**: Are all dependencies up to date?
- **CVE Check**: Do any dependencies have known vulnerabilities?
- **Supply Chain**: Are dependencies from trusted sources (PyPI, npm)?

### 10. Insufficient Logging & Monitoring
- **Security Events**: Are login attempts, access failures logged?
- **Audit Trail**: Is there an audit trail for sensitive operations?
- **Monitoring**: Are anomalies detected and alerted?

## AI/ML Security Specific

### Model Security
- **Model Poisoning**: Is training data validated?
- **Adversarial Inputs**: Are there safeguards against adversarial examples?
- **Model Theft**: Are model endpoints protected from extraction attacks?

### API Security
- **Rate Limiting**: Are API endpoints rate-limited to prevent abuse?
- **API Key Security**: Are API keys stored securely and rotated regularly?
- **Token Limits**: Are there limits on LLM token usage to prevent cost abuse?
- **Input Validation**: Is LLM input validated for malicious prompts?

### Data Privacy
- **PII Handling**: Is personally identifiable information handled properly?
- **Data Retention**: Is data deleted when no longer needed?
- **Encryption**: Is sensitive data encrypted at rest and in transit?
- **Vector Database**: Are embeddings containing sensitive data protected?

## Infrastructure Security

### Docker/Container Security
- **Base Images**: Are official, minimal base images used?
- **Running as Root**: Are containers running as non-root users?
- **Secrets in Images**: Are secrets excluded from Docker images?
- **Image Scanning**: Are images scanned for vulnerabilities?

### Network Security
- **HTTPS**: Is HTTPS enforced for all communications?
- **TLS Version**: Is TLS 1.2+ used?
- **Certificate Validation**: Are SSL certificates validated?
- **Internal Services**: Are internal services protected from public access?

### Environment & Configuration
- **Environment Files**: Is `.env` in `.gitignore`?
- **Secret Management**: Are secrets managed properly (not in code)?
- **Least Privilege**: Do services run with minimal required permissions?

## Code Security Patterns

### Input Validation
- Are all inputs validated (type, length, format, range)?
- Is there a whitelist approach for allowed values?
- Are file uploads restricted by type and size?

### Output Encoding
- Is output properly encoded for the context (HTML, JSON, SQL)?
- Are templates auto-escaping by default?

### Error Handling
- Are errors caught without exposing stack traces to users?
- Are generic error messages shown to users?
- Are detailed errors logged server-side only?

### Dependencies
```bash
# Check for vulnerable dependencies
pip-audit  # for Python
npm audit  # for Node.js
```

---

## Security Review Format

Please provide:

1. **Critical Issues**: Vulnerabilities that MUST be fixed before merging (e.g., exposed secrets, SQL injection)
2. **High Priority**: Security issues that should be fixed soon (e.g., weak authentication, missing validation)
3. **Medium Priority**: Security improvements recommended (e.g., add rate limiting, improve logging)
4. **Low Priority**: Security best practices to consider (e.g., security headers, better error messages)
5. **Positive Findings**: Security controls that are implemented well
6. **Verdict**: APPROVE, REQUEST CHANGES (if critical/high issues), or COMMENT

For each issue:
- Specify the file and line number
- Explain the vulnerability and potential impact
- Provide a concrete fix or mitigation

Be thorough and specific. Security issues should block merging until resolved.
