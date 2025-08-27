# conftest.py

from pathlib import Path

import pytest

from marimo_job_scraper.scrapers.python_jobs_github_scraper import (
    PythonJobsGithubScraper,
)


@pytest.fixture
def sample_html() -> str:
    """Fixture to load the sample html file."""
    filename = "pythonjobsgithub_sample.html"
    filepath: Path = Path(__file__).parent / "fixtures" / filename

    if not filepath.exists():
        raise FileNotFoundError(f"Fixture file not found: {filepath}")

    content = filepath.read_text(encoding="utf-8")

    return content


@pytest.fixture
def scraper() -> PythonJobsGithubScraper:
    return PythonJobsGithubScraper()
