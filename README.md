# Better-Brighter: Electricity Utility Record Anomaly Detection

Better-Brighter is a proposed machine learning-based project that aims to help data quality officers identify unusual electricity utility records for further review. It focuses on detecting potential data quality issues and presenting flagged records in a clear, organised way.

> **Project stage:** Planning and portfolio preparation (CSC649). This repository documents the project scope, requirements, user stories, technology evaluation and development plan. It does not yet represent a completed production system.

## Problem statement

Electricity utility organisations rely on accurate meter readings and customer records for reporting and operational decision-making. However, records may contain missing values, duplicate entries, inconsistent information or unusual meter-reading patterns. Finding these issues through manual checking can take time and may make it harder for data quality officers to prioritise records that need attention. Better-Brighter proposes an anomaly-detection approach to flag unusual records for human investigation; it will not automatically alter original readings or make billing decisions.

## Project documents

- [Problem statement](docs/problem-statement.md)
- [Requirements](docs/requirements.md)
- [User stories](docs/user-stories.md)
- [Sprint log](docs/sprint-log.md)
- [Technology stack evaluation](docs/tech-stack-evaluation.md)
- [Week 4 testing and CI/CD notes](docs/testing-and-cicd.md)

## Proposed technology

The proposed prototype uses Python for data processing and machine learning, with scikit-learn for anomaly detection and a relational database for storing sample records and validation results. A lightweight web interface may be used to review flagged records and their status. The final choice will be guided by the requirements, available time and the technology evaluation documented in this repository.

## Project scope

**Included:** sample or synthetic electricity utility records, exploratory data preparation, rule-based data checks, anomaly detection experiments, flagged-record review and summary reporting.

**Not included:** access to confidential live utility databases, automatic changes to actual meter readings, automated billing decisions or production deployment.

## Repository structure

```text
.
├── README.md
├── .gitignore
├── docs/
│   ├── problem-statement.md
│   ├── requirements.md
│   ├── user-stories.md
│   ├── sprint-log.md
│   ├── tech-stack-evaluation.md
│   └── testing-and-cicd.md
└── src/
    └── README.md
```

## Quality and workflow

The Week 4 lab provides a practice example of writing unit tests and running them through GitHub Actions. Any test result reported for Better-Brighter must come from tests written for this repository. The sample Week 4 study-planner tests are not evidence that the anomaly-detection project has passed its own tests.

## Current status

- [x] Project repository created
- [x] Problem statement, requirements and user stories documented
- [x] Source and documentation folders organised
- [ ] Finalise technology evaluation
- [ ] Define project-specific test cases
- [ ] Implement and evaluate the anomaly-detection prototype
- [ ] Configure and verify GitHub Actions for this project
- [ ] Publish a project portfolio page, if required

## Author

Muhamad Dahnial bin Mohd Tahir
