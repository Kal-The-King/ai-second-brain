from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import SecondBrain

app = FastAPI(title="AI Second Brain Advanced")
brain = SecondBrain()

class MemoryInput(BaseModel):
    text: str

class SearchInput(BaseModel):
    query: str

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "advanced-ai-second-brain"}

@app.post("/remember")
def remember(payload: MemoryInput):
    result = brain.store_memory(payload.text)
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
