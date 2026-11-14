# Better-Brighter: Machine Learning for Anomaly Detection in Electricity Utility Records

Better-Brighter is an academic project that explores how data-quality checks and machine learning can help data quality officers identify unusual electricity utility records for further review.

> **Project status:** Portfolio and prototype stage for CSC649. The repository contains project documentation, a small Python demonstration, automated tests and a GitHub Actions workflow. It is not a production utility system.

[![Better-Brighter CI](https://github.com/DahnialTahir97/Better-Brigter/actions/workflows/ci.yml/badge.svg)](https://github.com/DahnialTahir97/Better-Brigter/actions/workflows/ci.yml)

## Problem statement

Electricity utility organisations depend on reliable meter-reading and customer records for reporting and operational activities. However, records may contain missing information, duplicates, inconsistent formats or unusual reading patterns that are not always easy to identify through manual checking. These issues can increase the workload of data quality officers and affect confidence in information used for analysis. Better-Brighter explores a data-quality and anomaly-detection approach that flags unusual records for human review without changing original readings or making billing decisions.

## Project objectives

1. Identify common data-quality issues in sample electricity utility records.
2. Apply basic validation rules to detect missing fields, duplicate identifiers and invalid readings.
3. Explore Isolation Forest to flag unusual numerical readings for further review.
4. Organise findings so that users can understand why a record was flagged.

## Technology stack

| Technology | Purpose |
|---|---|
| Python | Main programming language for the prototype |
| pandas | Data handling and preparation |
| scikit-learn | Isolation Forest anomaly-detection experiment |
| pytest | Automated unit testing |
| GitHub Actions | Continuous integration and automated test execution |
| GitHub Pages | Static project portfolio page |

A Flask dashboard and relational database may be considered as future extensions. They are not required for the current small demonstration.

## Repository contents

- [Problem statement](docs/problem-statement.md)
- [Requirements](docs/requirements.md)
- [User stories and acceptance criteria](docs/user-stories.md)
- [Sprint log](docs/sprint-log.md)
- [Technology stack evaluation](docs/tech-stack-evaluation.md)
- [Testing and CI/CD plan](docs/testing-and-cicd.md)
- [Source code](src/)
- [Automated tests](tests/)
- [Portfolio website source](site/index.html)
- [GitHub Actions workflows](.github/workflows/)

## Testing and project status

The CI workflow runs the project's own pytest suite on pushes to `main` and pull requests. Check the [Actions tab](https://github.com/DahnialTahir97/Better-Brigter/actions) for the latest actual result; do not use the Week 4 study-planner starter's test count as a Better-Brighter result.

The static portfolio page is prepared for GitHub Pages. Once Pages is enabled with **GitHub Actions** as the build and deployment source and the deployment workflow succeeds, it should be available at:

[Better-Brighter GitHub Pages](https://dahnialtahir97.github.io/Better-Brigter/)

## Scope and limitations

- Development and demonstration use synthetic sample data only.
- The prototype does not connect to confidential or live electricity utility databases.
- An anomaly flag indicates an unusual pattern; it does not prove that a record is incorrect.
- The prototype does not modify original meter readings or make billing decisions.
- This repository demonstrates the project portfolio and a small technical proof of concept, not a complete production system.

## Author

**Muhamad Dahnial bin Mohd Tahir**
