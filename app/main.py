from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from app.brain.second_brain import SecondBrain
from app.config import BING_SEARCH_KEY, OPENAI_API_KEY
from app.services.web_service import EmbeddingService

app = FastAPI(
    title="AI Second Brain Production",
    description="Production-grade semantic memory + web search brain for AI agents",
    version="1.0.0"
)

# CORS for easy deployment on any website
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize embedding service
embedding_service = EmbeddingService(api_key=OPENAI_API_KEY)

class MemoryInput(BaseModel):
    text: str
    category: str = "general"
    source: str = "user"
    tags: Optional[List[str]] = None
    importance: float = 0.5

class SearchInput(BaseModel):
    query: str
    limit: int = 5

class RecallAndSearchInput(BaseModel):
    query: str
    local_limit: int = 3
    web_limit: int = 3

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "second-brain-production"}

@app.post("/remember")
def remember(payload: MemoryInput, user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    result = brain.remember(payload.text, payload.category, payload.source, payload.tags, payload.importance)
    return {"status": "saved", "memory": result}

@app.post("/recall")
def recall(payload: SearchInput, user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    results = brain.recall(payload.query, payload.limit)
    return {"query": payload.query, "results": results}

@app.post("/search-web")
def search_web(payload: SearchInput, user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    results = brain.search_web(payload.query, payload.limit)
    return {"query": payload.query, "results": results}

@app.post("/recall-and-search")
def recall_and_search(payload: RecallAndSearchInput, user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    results = brain.recall_and_search(payload.query, payload.local_limit, payload.web_limit)
    return {"query": payload.query, "results": results}

@app.post("/chat")
def chat(payload: MemoryInput, user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    response = brain.reply(payload.text)
    return {"response": response}

@app.get("/memory")
def list_memory(user_id: Optional[str] = None):
    brain = SecondBrain(user_id=user_id, bing_key=BING_SEARCH_KEY, embedding_service=embedding_service)
    return {"memory": brain.list_all_memory()}
