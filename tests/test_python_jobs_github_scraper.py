# test_python_jobs_github_scraper.py

import pytest

from marimo_job_scraper.scrapers.python_jobs_github_scraper import (
    PythonJobsGithubScraper,
)


@pytest.fixture
def scraper() -> PythonJobsGithubScraper:
    return PythonJobsGithubScraper()


def test_fetch_returns_response(scraper):
    response = scraper.fetch()
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]


def test_parse_returns_list(scraper):
    response = scraper.fetch()
    jobs = scraper.parse(response)
    assert isinstance(jobs, list)
