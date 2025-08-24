# test_python_jobs_github_scraper.py

from pathlib import Path

import pytest
from bs4 import BeautifulSoup, ResultSet, Tag

from marimo_job_scraper.scrapers.python_jobs_github_scraper import (
    PythonJobsGithubScraper,
)


@pytest.fixture
def sample_html() -> str:
    """Fixture to load the sample html file."""
    filename = "pythonjobsgithub_sample.html"
    filepath: Path = Path(__file__).parent.parent / "tests" / "fixtures" / filename
    with filepath.open("r", encoding="utf-8") as file:
        return file.read()


@pytest.fixture
def scraper() -> PythonJobsGithubScraper:
    return PythonJobsGithubScraper()


def test_fetch_returns_response(scraper):
    response = scraper.fetch()
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]


def test_parse_returns_list(scraper, sample_html):
    jobs = scraper.parse(sample_html)
    assert isinstance(jobs, list)


def test_parse_none_returns_empty_list(scraper):
    jobs = scraper.parse(None)
    assert jobs == []


def test_parse_returns_non_empty_list(scraper, sample_html):
    jobs = scraper.parse(sample_html)
    assert jobs != [], "jobs should not be an empty list."


def test_parse_job_card_returns_dict(scraper, sample_html):
    # Get first job_card from html
    soup: BeautifulSoup = BeautifulSoup(sample_html, features="html.parser")
    job_section: Tag = soup.find("section", class_="job_list")
    job_card: ResultSet = job_section.find("div", class_="job")

    assert isinstance(scraper._parse_job_card(job_card), dict)
