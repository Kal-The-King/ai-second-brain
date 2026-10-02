from app.memory.store import MemoryStore


class MemoryManager:
    def __init__(self, store: MemoryStore | None = None):
        self.store = store or MemoryStore()

    def save(self, text: str, category: str = "general"):
        return self.store.add(text, category=category)

    def recall(self, query: str):
        return self.store.search(query)

    def all(self):
        return self.store.list()

    def clear(self):
        self.store.clear()
