# Marimo Based Job Scraper

## Tests

- These use `pytest`.
- `conftest.py` defines the fixtures and makes them available to the test suite.
- `pytest.ini` registers the markers used.

### Run tests

- Run all tests. From the project root:
  
  ```shell
  uv run pytest tests
  ```

- Run all tests except those marked as integration tests (to avoid frequent `GET` requests to the server).
  
  ```shell
  uv run pytest tests -m "not integration"
  ```
