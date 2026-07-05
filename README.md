# GEO Agent

[![CI](https://github.com/kogunlowo123/geo-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/geo-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Generative Engine Optimization agent that optimizes content for AI search engines and LLM-powered answer systems, ensuring brand visibility in AI-generated summaries and citations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `audit_ai_visibility` | Audit brand visibility in AI search results and chatbot responses |
| `optimize_for_llm` | Optimize content structure for LLM citation and extraction |
| `track_ai_mentions` | Track brand mentions in AI-generated content |
| `generate_structured_data` | Generate structured data markup for AI crawlers |
| `benchmark_competitors` | Benchmark AI visibility against competitors |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/geo/create` | Create or generate |
| `POST` | `/api/v1/geo/analyze` | Analyze performance |
| `POST` | `/api/v1/geo/optimize` | Optimize |
| `POST` | `/api/v1/geo/schedule` | Schedule |
| `POST` | `/api/v1/geo/report` | Generate report |

## Features

- Geo
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
geo-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── geo_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
