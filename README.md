# AI Second Brain Production - Semantic + Web Search

A production-grade AI second brain with:
- **Semantic memory** with embeddings for intelligent recall
- **Wide web search** with Bing API
- **Page fetching and caching** for faster retrieval
- **CORS enabled** for easy embedding on any website
- **REST API** for integration with any AI agent
- **User profiles** for per-user memory isolation

## Quick Start

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add your API keys:
# BING_SEARCH_KEY=your_bing_key
# OPENAI_API_KEY=your_openai_key
# DATABASE_URL=sqlite:///./brain.db  # or PostgreSQL URL

# Run
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /remember` - Store memory
- `POST /recall` - Search local memory semantically
- `POST /search-web` - Search the internet
- `POST /recall-and-search` - Combined local + web search
- `GET /memory` - List all memories
- `POST /chat` - Chat with the brain
- `GET /health` - Health check

## Example Usage

```python
from app.brain import SecondBrain

brain = SecondBrain(user_id="user-123")
brain.remember("Python is a powerful programming language", category="tech")
results = brain.recall("programming", limit=5)
web_results = brain.search_web("latest Python trends", limit=5)
print(results, web_results)
```

## Embed in Website

```html
<script src="https://your-brain-domain/sdk.js"></script>
<div id="second-brain"></div>
<script>
    SecondBrain.init('user-123', 'https://your-brain-api.com');
    SecondBrain.widget('#second-brain');
</script>
```

## Deployment

### Docker

```bash
docker build -t second-brain .
docker run -p 8000:8000 -e BING_SEARCH_KEY=xxx second-brain
```

### Cloud Platforms

- **Heroku**: `git push heroku main`
- **Railway**: Connect GitHub repo
- **AWS Lambda**: Use Zappa
- **Google Cloud**: Cloud Run

## Next Steps

- Add PostgreSQL + pgvector for true semantic search
- Implement memory pruning and summarization
- Add privacy controls and encryption
- Build admin dashboard for memory management
- Add multi-modal support (images, files, PDFs)

## Architecture

```
SecondBrain
├── SemanticMemory (local + embeddings)
├── WebBrain (internet search + caching)
├── UserProfile (per-user settings)
└── Services
    ├── EmbeddingService (OpenAI)
    ├── WebSearchService (Bing)
    └── PageFetcher (fetch & cache pages)
```

## License

MIT
