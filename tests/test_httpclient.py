# test_httpclient.py
import pytest

from marimo_job_scraper.utils.httpclient import HTTPClient


def test_get_returns_response():
    url = "https://httpbin.org/get"
    response = HTTPClient.get(url)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]


@pytest.mark.parametrize("status_code", [404, 500, 503])
def test_get_returns_none_for_error_status(status_code):
    url = "https://httpbin.org/status/{status_code}"
    response = HTTPClient.get(url)
    assert response is None
