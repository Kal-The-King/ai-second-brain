import uuid
import requests
from datetime import datetime
from typing import Optional, List
import json


class EmbeddingService:
    def __init__(self, api_key: str = None, model: str = "text-embedding-3-small"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.openai.com/v1/embeddings"

    def embed(self, text: str) -> Optional[List[float]]:
        if not self.api_key:
            return None
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"input": text, "model": self.model}
        response = requests.post(self.base_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["data"][0]["embedding"]
        return None


class WebSearchService:
    def __init__(self, bing_key: str = None):
        self.bing_key = bing_key
        self.bing_url = "https://api.bing.microsoft.com/v7.0/search"

    def search(self, query: str, count: int = 10) -> List[dict]:
        if not self.bing_key:
            return []
        headers = {"Ocp-Apim-Subscription-Key": self.bing_key}
        params = {"q": query, "count": count}
        response = requests.get(self.bing_url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json().get("webPages", {}).get("value", [])
            return [{"url": r["url"], "title": r["name"], "snippet": r["snippet"]} for r in results]
        return []


class PageFetcher:
    def fetch(self, url: str, timeout: int = 15) -> Optional[str]:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            return text[:10000]
        except Exception:
            return None


class Summarizer:
    def summarize(self, text: str, max_sentences: int = 5) -> str:
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        return " ".join(sentences[:max_sentences])
