# test_httpclient.py
import pytest

from marimo_job_scraper.utils.httpclient import HTTPClient


def test_get_returns_response():
    url = "https://httpbin.org/get"
    response = HTTPClient.get(url)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
