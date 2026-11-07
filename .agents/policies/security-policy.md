# Security Policy

This policy governs how agents handle sensitive data, credentials, and external communications within the harness.

## Sensitive Data Handling

### PII and Project Data
- The founder may share sensitive data (user PII, business data, specific requirements) in conversation to provide context.
- **Never use sensitive data directly** in any artifact, document, or code. Anonymize, generalize, or abstract it.
- If sensitive data must be referenced, use placeholders (e.g., `[USER_EMAIL]`, `[COMPANY_NAME]`) and note that real values should be substituted by the founder.
- When generating examples for PRDs, user stories, or test cases, use fictional data — never echo back real data the founder provided.

### Data in Documents
- PRDs and requirements pushed to Confluence/Notion must not contain raw PII or credentials.
- If the founder pastes sensitive content for context, extract the requirement or intent, discard the raw data.

## Credentials and Environment Variables

### Before Starting Any Process
When a founder begins working on a local project repository, agents must:
1. Check if `.env` file exists and required values are set
2. If values are missing, ask the founder to provide them
3. Help set the values in `.env`
4. **Verify that `.env` is in `.gitignore`** before any git operation

### Hard Rules
- **Never commit `.env` files or any file containing secrets to git.** This is non-negotiable.
- **Never hardcode** API keys, tokens, passwords, or credentials in any source file.
- **Never log** credential values in output, traces, or audit logs.
- Always use `.env.example` with placeholder values as the committed reference.
- Before any `git add` or `git commit`, scan staged files for potential secrets (API keys, tokens, connection strings). If found, abort and alert the founder.

### Key Rotation
- If a credential is accidentally exposed (in logs, output, or a commit), immediately flag it to the founder and recommend rotation.

## Third-Party Tool Communication

### Transparency Principle
Before sending any data to an external tool or API (Notion, Confluence, Jira, Linear, GitHub, or any other service):

1. **Call out clearly** what data will be sent
2. **Name the destination** — which tool, which endpoint, which workspace
3. **Show the payload** — let the founder see exactly what is being transmitted
4. **Ask for explicit permission** — wait for approval before sending
5. **Allow modification** — the founder may want to redact or change specific fields before transmission

### Per-Request Consent
- Each data transmission requires its own consent. Approval for one API call does not extend to subsequent calls.
- Bulk operations (e.g., creating 20 user stories in Jira) may be approved as a batch, but the full payload must be shown first.

### Data Minimization
- Only send the minimum data required for the operation. Do not include extra fields "just in case."
- If a tool's API accepts optional fields, only populate what is necessary.

## Git Security

### Pre-Commit Checks
Before every commit, verify:
- No `.env` or secret files are staged
- No hardcoded credentials in source files
- No PII in committed artifacts
- `.gitignore` includes all sensitive patterns

### Patterns That Must Be in .gitignore
```
.env
.env.local
.env.*.local
*.pem
*.key
*.secret
local-data/
```

## Network and Access

- Agents must not access URLs, endpoints, or services not explicitly configured or approved by the founder.
- If a workflow requires a new external service, propose it to the founder with rationale before making any connection.
- All integrations must use the credentials from `.env` — never prompt for credentials inline.

## Incident Response

If a security issue is detected (leaked credential, PII in a commit, unauthorized data transmission):
1. Stop all current operations immediately
2. Report the issue to the founder with full details
3. Recommend remediation steps
4. Do not attempt to fix silently
