# abstract_job_scraper.py

from abc import ABC, abstractmethod
from typing import Any, Self


class JobScraper(ABC):
    def __init__(self: Self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def fetch(self: Self) -> Any:
        """Fetch html response from website."""

    @abstractmethod
    def parse(self: Self, raw_html: Any) -> list[dict]:
        """Parse html into a list of job dicts."""

    def scrape(self: Self) -> list[dict]:
        """Convenience method to scrape jobs and return a list of job dicts."""
        response: Any = self.fetch()
        return self.parse(raw_html=response.content)
