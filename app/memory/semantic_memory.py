import uuid
from typing import List, Optional
from datetime import datetime
from app.db import SessionLocal, Memory, WebCache, UserProfile
from app.services.web_service import EmbeddingService


class SemanticMemory:
    def __init__(self, embedding_service: EmbeddingService = None):
        self.db = SessionLocal()
        self.embedding_service = embedding_service or EmbeddingService()

    def store(self, text: str, category: str = "general", source: str = "user", tags: List[str] = None, importance: float = 0.5) -> dict:
        memory_id = str(uuid.uuid4())
        embedding = self.embedding_service.embed(text) if self.embedding_service else None
        memory = Memory(
            id=memory_id,
            text=text,
            category=category,
            source=source,
            tags=tags or [],
            embedding=embedding,
            importance_score=importance
        )
        self.db.add(memory)
        self.db.commit()
        return {"id": memory_id, "text": text, "category": category, "source": source}

    def search(self, query: str, limit: int = 5) -> List[dict]:
        query_embedding = self.embedding_service.embed(query) if self.embedding_service else None
        results = self.db.query(Memory).all()
        
        if query_embedding:
            # Semantic similarity search
            scored_results = []
            for memory in results:
                if memory.embedding:
                    similarity = self._cosine_similarity(query_embedding, memory.embedding)
                    scored_results.append({"id": memory.id, "text": memory.text, "category": memory.category, "score": similarity})
            scored_results.sort(key=lambda x: x["score"], reverse=True)
            return scored_results[:limit]
        else:
            # Fallback to keyword search
            q = query.lower()
            keyword_results = [r for r in results if q in r.text.lower()]
            return [{"id": r.id, "text": r.text, "category": r.category, "score": 0} for r in keyword_results[:limit]]

    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = sum(a ** 2 for a in vec1) ** 0.5
        magnitude2 = sum(b ** 2 for b in vec2) ** 0.5
        return dot_product / (magnitude1 * magnitude2 + 1e-10) if magnitude1 and magnitude2 else 0.0

    def list_all(self) -> List[dict]:
        memories = self.db.query(Memory).all()
        return [{"id": m.id, "text": m.text, "category": m.category, "source": m.source} for m in memories]

    def delete(self, memory_id: str) -> bool:
        self.db.query(Memory).filter(Memory.id == memory_id).delete()
        self.db.commit()
        return True
