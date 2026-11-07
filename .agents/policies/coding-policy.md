# Coding Policy

This policy defines coding standards for the harness itself and for projects built through it.

## Harness Codebase (This Repository)

### Language & Runtime
- **Python 3.11+** is the primary language for the harness
- Use type hints for all public functions and class attributes
- Follow PEP 8 style guidelines
- Use `ruff` for linting and formatting

### Project Structure
- Keep modules focused — one responsibility per file
- Use `__init__.py` to define public APIs for packages
- Prefer composition over inheritance
- Keep functions small and testable

### Dependencies
- Pin all dependency versions in `pyproject.toml`
- Minimize external dependencies — every dependency is a maintenance burden
- Prefer standard library solutions when they're adequate
- Document why each dependency is needed

### Documentation
- Docstrings for all public functions and classes (one line if simple, multi-line if complex)
- No inline comments unless explaining a non-obvious "why"
- README in each major directory explaining its purpose

### Testing
- Testing philosophy to be defined per project by the founder
- At minimum, MCP tools and workflow logic must have tests
- Tests live in `tests/` mirroring the source structure

## Projects Built Through the Harness

The harness supports building projects in multiple tech stacks. When generating code, architecture, or technical artifacts for a project, use the standards for that project's stack.

### Supported Stacks

| Stack | Language | Framework | Use Case |
|---|---|---|---|
| Java | Java 17+ | Spring Boot | Backend services, enterprise APIs |
| JavaScript/TypeScript | ES2022+ / TS 5+ | React | Frontend SPAs |
| JavaScript/TypeScript | ES2022+ / TS 5+ | Angular | Frontend enterprise apps |
| JavaScript/TypeScript | ES2022+ / TS 5+ | Node.js (Express/Fastify) | Backend APIs |
| JavaScript/TypeScript | ES2022+ / TS 5+ | Next.js | Full-stack web apps |
| Python | Python 3.11+ | FastAPI | Backend APIs, microservices |

### Stack-Agnostic Standards
Regardless of the project's stack, always:
- Follow the stack's idiomatic conventions and community best practices
- Use the project's chosen package manager and build tooling
- Write clean, readable code — favor clarity over cleverness
- Handle errors explicitly — no silent failures
- Use environment variables for configuration — never hardcode
- Follow the security policy for credential handling
- Generate code that is production-ready, not prototype-quality

### Stack Selection
- The founder decides the tech stack for each project
- Agents may recommend a stack with rationale but must not assume
- Once a stack is chosen, all technical artifacts must be consistent with it

## Code Generation Guidelines

When agents generate code (in later ADLC phases):
- Generate complete, working code — not snippets with "TODO" markers
- Include error handling appropriate to the context
- Follow the project's established patterns — read existing code before generating new code
- If generating code that interacts with external services, use the configured integration layer
- Never generate code that bypasses the security policy
