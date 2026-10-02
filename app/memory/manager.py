from app.memory.store import MemoryStore


class MemoryManager:
    def __init__(self, store: MemoryStore | None = None):
        self.store = store or MemoryStore()

    def save(self, text: str):
        return self.store.add(text)

    def recall(self, query: str):
        return self.store.search(query)

    def all(self):
        return self.store.list()
