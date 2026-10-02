from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import SecondBrain
from app.web import WebKnowledge

app = FastAPI(title="AI Second Brain Advanced")
brain = SecondBrain()
web_knowledge = WebKnowledge()

class MemoryInput(BaseModel):
    text: str
    category: str = "general"
    source: str | None = None
    tags: list[str] | None = None

class SearchInput(BaseModel):
    query: str

class WebInput(BaseModel):
    url: str
    content: str

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "advanced-ai-second-brain"}

@app.post("/remember")
def remember(payload: MemoryInput):
    result = brain.store_memory(payload.text, category=payload.category, source=payload.source, tags=payload.tags)
    return {"status": "saved", "memory": result}

@app.post("/search")
def search(payload: SearchInput):
    results = brain.retrieve_memory(payload.query)
    return {"query": payload.query, "results": results}

@app.post("/chat")
def chat(payload: MemoryInput):
    response = brain.reply(payload.text)
    return {"response": response}

@app.get("/memory")
def memory():
    return {"memory": brain.list_memory()}

@app.get("/memory/summary")
def memory_summary():
    return {"summary": brain.summarize_memory()}

@app.post("/web-cache")
def web_cache(payload: WebInput):
    cached = web_knowledge.fetch(payload.url, payload.content)
    return {"status": "cached", "result": cached}
