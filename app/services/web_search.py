from pathlib import Path

from bs4 import BeautifulSoup
import requests


class WebSearchService:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    def fetch_text(self, url: str) -> str:
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        return text[:6000]

    def summarize(self, content: str) -> str:
        sentences = [s.strip() for s in content.replace("\n", " ").split(".") if s.strip()]
        return " ".join(sentences[:5])
