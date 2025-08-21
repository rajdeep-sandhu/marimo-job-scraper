# test_python_jobs_github_scraper.py

import pytest

from marimo_job_scraper.scrapers.python_jobs_github_scraper import (
    PythonJobsGithubScraper,
)


@pytest.fixture
def scraper() -> PythonJobsGithubScraper:
    return PythonJobsGithubScraper
