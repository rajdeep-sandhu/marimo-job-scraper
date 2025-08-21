# python_jobs_github_scraper.py
from datetime import datetime
from typing import Self

import requests
from bs4 import BeautifulSoup, ResultSet, Tag
from requests import Response, Session

from marimo_job_scraper.scrapers.abstract_job_scraper import JobScraper


class PythonJobsGithubScraper(JobScraper):
    """Concrete scraper for https://pythonjobs.github.io/."""

    def __init__(self: Self, base_url: str = "https://pythonjobs.github.io/"):
        """Constructor."""
        super().__init__(base_url=base_url)

    def fetch(self: Self) -> Response:
        """Fetch response from url."""
        response: Response = requests.get(url=self.base_url)
        response.raise_for_status()
        return response

    def parse(self: Self, raw_html: Response) -> list[dict]:
        """Parse html into a list of job dicts."""
        raise NotImplementedError
