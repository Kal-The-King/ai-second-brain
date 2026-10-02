# AI Second Brain Advanced

This version improves the second brain by adding:
- richer memory metadata (category, source, tags)
- ranked memory search results
- memory summary generation
- web content caching and fetch support
- better extensibility for future semantic memory and external search

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example

```python
from app.brain import SecondBrain

brain = SecondBrain()
brain.store_memory("The user prefers concise, structured answers.", category="preferences", source="conversation", tags=["style", "answers"])
print(brain.reply("What format do I like?"))
print(brain.summarize_memory())
```

## Next upgrade suggestions
- PostgreSQL + pgvector for semantic memory
- proper web research pipeline
- notebook or app UI for memory browsing
- user profile memory with privacy controls
