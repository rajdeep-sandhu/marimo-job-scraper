# sample_html_fixture_creator.py
from pathlib import Path

import requests

from marimo_job_scraper.scrapers import JobScraper, PythonJobsGithubScraper
from marimo_job_scraper.utils import HTTPClient


def main():
    file_scrapers: dict = {"pythonjobsgithub_sample_download.html": PythonJobsGithubScraper()}

    for file, scraper in file_scrapers.items():
        response: requests.Response = scraper.fetch()
        # tests\fixtures\pythonjobsgithub_sample.html
        file_path = Path(__file__).parent / file
        print(file_path)

        if not file_path.exists():
            with open(file_path, mode="w", encoding="utf-8") as f:
                f.write(response.text) 
            print(f"Created {file}.")
        else:
            print(f"{file_path} already exists.")


if __name__ == "__main__":
    main()
