# python_jobs_github_scraper.py
import logging
from datetime import datetime
from http import HTTPMethod, HTTPStatus
from typing import Any, Self

import requests
from bs4 import BeautifulSoup, ResultSet, Tag
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry

from marimo_job_scraper.scrapers.abstract_job_scraper import JobScraper
from marimo_job_scraper.utils.httpclient import HTTPClient


class PythonJobsGithubScraper(JobScraper):
    """Concrete scraper for https://pythonjobs.github.io/."""

    def __init__(self: Self, base_url: str = "https://pythonjobs.github.io/"):
        """Constructor."""
        super().__init__(base_url=base_url)

    def fetch(self: Self) -> Response | None:
        """Fetch response from url."""

        return HTTPClient.get(url=self.base_url)

    def _parse_job_card(self: Self, job_card: Tag) -> dict[Any]:
        """
        Parse job_card into dict.
        Parsing logic is by necessity tightly coupled to the html structure of the site.
        """

        data_tags: list[str] = job_card.attrs.get("data-tags", "").strip().split(",")
        link: str = f"{self.base_url[:-1]}{job_card.h1.a['href']}"
        title: str = job_card.h1.a.text.strip()

        # Parse info items
        info_items: list[Tag] = job_card.find_all("span", class_="info")
        info: dict = {item.i["class"][0]: item.text.strip() for item in info_items}

        # Set job_date to None if not in info or if not formatted as 'Tue, 23 Nov 2021'.
        job_date: datetime.date = None
        if info.get("i-calendar"):
            try:
                job_date = datetime.strptime(
                    info["i-calendar"].strip(), "%a, %d %b %Y"
                ).date()
            except ValueError:
                job_date = None

        detail: str = job_card.find("p", class_="detail").text.strip()

        return {
            "title": title,
            "company": info.get("i-company", "").strip(),
            "location": info.get("i-globe", "").strip(),
            "tenure": info.get("i-chair", "").strip(),
            "date": job_date,
            "detail": detail,
            "data_tags": data_tags,
        }

    def parse(self: Self, raw_html: str | bytes) -> list[dict]:
        """Parse html into a list of job dicts."""

        if (not raw_html) or (raw_html is None):
            return []

        # Get job_cards from html
        soup: BeautifulSoup = BeautifulSoup(raw_html, features="html.parser")
        job_section: Tag = soup.find("section", class_="job_list")
        job_cards: ResultSet = job_section.find_all("div", class_="job")

        # Parse job data into a list of dicts.
        jobs: list[dict] = [self._parse_job_card(job_card) for job_card in job_cards]

        return jobs


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
    )
    logger.addHandler(handler)
