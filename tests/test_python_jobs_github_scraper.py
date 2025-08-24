# test_python_jobs_github_scraper.py

from pathlib import Path

import pytest

from marimo_job_scraper.scrapers.python_jobs_github_scraper import (
    PythonJobsGithubScraper,
)


@pytest.fixture
def sample_html() -> str:
    """Fixture to load the sample html file."""
    filename = "pythonjobsgithub_sample.html"
    filepath: Path = (
        Path(__file__).parent.parent / "tests" / "fixtures" / filename
    )
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


def test_parse_returns_non_empty_list(scraper):
    response = scraper.fetch()
    jobs = scraper.parse(response.content)
    assert jobs != [], "jobs should not be an empty list."
