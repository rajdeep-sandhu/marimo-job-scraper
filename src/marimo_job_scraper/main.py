import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from marimo_job_scraper.scrapers import JobScraper, PythonJobsGithubScraper
    return (PythonJobsGithubScraper,)


@app.cell
def _(PythonJobsGithubScraper):
    scraper = PythonJobsGithubScraper()
    scraper.scrape()
    return


if __name__ == "__main__":
    app.run()
