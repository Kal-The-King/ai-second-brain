from app.memory.semantic_memory import SemanticMemory
from app.brain.web_brain import WebBrain
from app.db import SessionLocal, UserProfile
import uuid


class SecondBrain:
    def __init__(self, user_id: str = None, bing_key: str = None, embedding_service = None):
        self.user_id = user_id or str(uuid.uuid4())
        self.db = SessionLocal()
        self.semantic_memory = SemanticMemory(embedding_service)
        self.web_brain = WebBrain(bing_key)
        self._ensure_user_profile()

    def _ensure_user_profile(self):
        user = self.db.query(UserProfile).filter(UserProfile.id == self.user_id).first()
        if not user:
            user = UserProfile(id=self.user_id, name=f"User {self.user_id[:8]}")
            self.db.add(user)
            self.db.commit()

    def remember(self, text: str, category: str = "general", source: str = "user", tags: list = None, importance: float = 0.5):
        return self.semantic_memory.store(text, category, source, tags, importance)

    def recall(self, query: str, limit: int = 5):
        return self.semantic_memory.search(query, limit)

    def search_web(self, query: str, limit: int = 5):
        return self.web_brain.search_and_cache(query, limit)

    def recall_and_search(self, query: str, local_limit: int = 3, web_limit: int = 3):
        local_results = self.recall(query, local_limit)
        web_results = self.search_web(query, web_limit)
        return {"local": local_results, "web": web_results}

    def reply(self, user_message: str):
        local_memory = self.recall(user_message, limit=3)
        if local_memory:
            context = "\n".join([f"- {m['text']}" for m in local_memory])
            return f"Relevant memory found:\n{context}"
        return f"No local memory. Try searching the web for: {user_message}"

    def list_all_memory(self):
        return self.semantic_memory.list_all()
