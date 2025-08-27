# test_python_jobs_github_scraper.py

import pytest
import requests
from bs4 import BeautifulSoup, ResultSet, Tag


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


def test_scrape(monkeypatch, scraper, sample_html):
    """
    Test the scrape() method.
    Mock fetch() and use sample_html.
    """

    class MockResponse:
        def __init__(
            self,
            content: bytes = b"",
            text: str = "",
            status_code: int = 200,
            headers: dict = None,
        ):
            self._content = content
            self.text = text
            self.status_code = status_code
            self.headers = headers or {"Content-Type": "text/html; charset=utf-8"}

        @property
        def content(self):
            """Return the raw content as bytes."""
            return self._content

    def mock_fetch():
        return MockResponse(
            content=sample_html.encode("utf-8"),
            text=sample_html,
            status_code=200,
            headers={"Content-Type": "text/html; charset=utf-8"},
        )

    monkeypatch.setattr(scraper, "fetch", mock_fetch)

    jobs = scraper.scrape()
    assert isinstance(jobs, list)
    assert len(jobs) > 0
    assert all(isinstance(job, dict) for job in jobs)


@pytest.mark.integration
def test_integration_live_fetch(scraper):
    """
    Test the scrape() method on live website.
    """

    jobs = scraper.scrape()
    assert isinstance(jobs, list)
    assert len(jobs) > 0
    assert all(isinstance(job, dict) for job in jobs)
