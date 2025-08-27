# sample_html_fixture_creator.py
from pathlib import Path

import requests

from marimo_job_scraper.scrapers import JobScraper, PythonJobsGithubScraper
from marimo_job_scraper.utils import HTTPClient


def scrape_to_file(filepath: Path, scraper: JobScraper) -> None:
    if filepath.exists():
        print(f"{filepath.parts[-1]} already exists.")
        return None

    response: requests.Response = scraper.fetch()
    filepath.write_text(data=response.text, encoding="utf-8")
    print(f"Created {filepath.parts[-1]}.")
    return None


def main():
    file_scrapers: dict = {
        "pythonjobsgithub_sample_download.html": PythonJobsGithubScraper
    }

    for file, ScraperClass in file_scrapers.items():
        filepath = Path(__file__).parent / file
        scrape_to_file(filepath=filepath, scraper=ScraperClass())


if __name__ == "__main__":
    main()
