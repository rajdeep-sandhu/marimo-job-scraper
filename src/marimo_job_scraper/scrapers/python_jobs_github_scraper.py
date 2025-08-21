# python_jobs_github_scraper.py
from datetime import datetime
from typing import Self

import requests
from bs4 import BeautifulSoup, ResultSet, Tag

from marimo_job_scraper.scrapers.abstract_job_scraper import JobScraper


class PythonJobsGithubScraper(JobScraper):
    """Concrete scraper for https://pythonjobs.github.io/."""

    def __init__(self: Self, base_url: str = "https://pythonjobs.github.io/"):
        super().__init__(base_url=base_url)
    
    def fetch(self: Self) -> requests.Response:
        pass

    def parse(self: Self, raw_html: requests.Response) -> list[dict]:
        """Parse html into a list of job dicts."""
        raise NotImplementedError
