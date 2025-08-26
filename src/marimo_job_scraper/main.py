import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from marimo_job_scraper.scrapers import JobScraper, PythonJobsGithubScraper
    return PythonJobsGithubScraper, mo


@app.cell
def _(PythonJobsGithubScraper):
    scraper = PythonJobsGithubScraper()
    jobs = scraper.scrape()
    return (jobs,)


@app.cell
def _(jobs, mo):
    table = mo.ui.table(jobs, selection='single', show_column_summaries='stats')
    return (table,)


@app.cell
def _(mo, table):
    mo.vstack([table, table.value])
    return


if __name__ == "__main__":
    app.run()
