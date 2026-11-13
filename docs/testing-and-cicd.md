# Testing and CI/CD

## Purpose
The Week 4 lab introduces unit testing, GitHub Actions and GitHub Pages deployment. Better-Brighter applies the same workflow ideas with tests written for this project's own functions.

## Local testing

```bash
pip install -r requirements.txt
pytest
```

The test suite covers required-field checks, duplicate identifiers, reading validation and the anomaly-detection demonstration. The authoritative result is the output from running the tests in this repository or the latest GitHub Actions run.

## Continuous integration
The workflow at `.github/workflows/ci.yml` runs pytest when code is pushed to `main` or a pull request is opened. A failing test causes the workflow to fail.

## Portfolio deployment
The workflow at `.github/workflows/pages.yml` publishes the static files in `site/` to GitHub Pages after changes are pushed to `main`. The static page is a project portfolio page; it does not host the Python application.

## Reporting status accurately
- **Test result:** report the count shown by the latest successful test run.
- **Latest Actions run:** report the actual status shown in the Actions tab.
- **Live page:** use the published URL only after GitHub Pages deployment succeeds and the page is accessible.

The Week 4 starter package's study-planner tests are teaching examples and must not be reported as tests of Better-Brighter.
