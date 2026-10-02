from fastapi import FastAPI
from pydantic import BaseModel
from app.brain import SecondBrain

app = FastAPI(title="AI Second Brain")
brain = SecondBrain()

class MessageInput(BaseModel):
    message: str

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ai-second-brain"}

@app.post("/chat")
def chat(input: MessageInput):
    response = brain.reply(input.message)
    return {"response": response}

@app.post("/remember")
def remember(input: MessageInput):
    brain.store_memory(input.message)
    return {"status": "saved", "memory": input.message}

@app.get("/memory")
def memory():
    return {"memory": brain.list_memory()}
