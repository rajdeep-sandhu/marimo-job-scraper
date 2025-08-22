# python_jobs_github_scraper.py
from datetime import datetime
from http import HTTPMethod, HTTPStatus
from typing import Self

import requests
from bs4 import BeautifulSoup, ResultSet, Tag
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry

from marimo_job_scraper.scrapers.abstract_job_scraper import JobScraper


class PythonJobsGithubScraper(JobScraper):
    """Concrete scraper for https://pythonjobs.github.io/."""

    def __init__(self: Self, base_url: str = "https://pythonjobs.github.io/"):
        """Constructor."""
        super().__init__(base_url=base_url)

    def fetch(self: Self) -> Response | None:
        """Fetch response from url."""

        # Define HTTPAdapter
        retry_strategy = Retry(
            total=3,
            status_forcelist=[
                HTTPStatus.NOT_FOUND,
                HTTPStatus.TOO_MANY_REQUESTS,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                HTTPStatus.BAD_GATEWAY,
                HTTPStatus.SERVICE_UNAVAILABLE,
                HTTPStatus.GATEWAY_TIMEOUT,
            ],
            allowed_methods=[HTTPMethod.GET],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)

        # Get request
        with Session() as session:
            session.mount(prefix=self.base_url, adapter=adapter)
            try:
                response: Response = session.get(url=self.base_url, timeout=3.01)
                response.raise_for_status()
                return response
            except requests.RequestException as err:
                return None
            finally:
                session.close()

    def parse(self: Self, raw_html: Response) -> list[dict]:
        """Parse html into a list of job dicts."""

        if (not raw_html) or (raw_html) is None:
            return []

        soup: BeautifulSoup = BeautifulSoup(raw_html.content, features="html.parser")
        job_section: Tag = soup.find("section", class_="job_list")
        job_cards: ResultSet = job_section.find_all("div", class_="job")

        jobs: list[dict] = []

        return jobs
