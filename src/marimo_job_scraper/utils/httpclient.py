# httpclient.py
from http import HTTPMethod, HTTPStatus

import requests
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry


class HTTPClient:
    """Utility class for making HTTP requests with retry logic."""

    DEFAULT_TIMEOUT = 3.01

    @staticmethod
    def fetch(url: str, timeout: float = DEFAULT_TIMEOUT):
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
            session.mount(prefix=url, adapter=adapter)
            try:
                response: Response = session.get(url=url, timeout=3.01)
                response.raise_for_status()
                return response
            except requests.RequestException as err:
                return None
