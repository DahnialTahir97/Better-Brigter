# Tech Stack Evaluation

## Project
Better-Brighter is a proposed prototype for checking electricity utility records and identifying unusual records for human review.

## Requirements that drive the decision
- **FR-01:** Import a structured sample dataset.
- **FR-04:** Identify invalid formats and reading values that break configured rules.
- **FR-05:** Apply an anomaly-detection method to suitable numerical fields.
- **NFR-03:** Use synthetic or shareable sample data rather than confidential live records.
- **NFR-04:** Keep validation and anomaly-detection logic readable and testable.
- **NFR-05:** Produce consistent findings for the same input and configuration.

## Options
- **Option A:** Python prototype using pandas and scikit-learn, with a lightweight command-line demonstration.
- **Option B:** Python web application using Flask, a relational database and a browser-based dashboard.
- **Option C:** Static website using HTML, CSS and JavaScript only.

## Decision matrix

Weight reflects importance (1 = low, 5 = high). Scores range from 1 (poor) to 5 (excellent). Weighted score = weight × score.

| Criterion | Weight | A score | A weighted | B score | B weighted | C score | C weighted |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fits project requirements | 5 | 5 | 25 | 5 | 25 | 1 | 5 |
| Skills and learning effort | 4 | 4 | 16 | 3 | 12 | 4 | 16 |
| Time to build | 5 | 5 | 25 | 3 | 15 | 5 | 25 |
| Free tools and local development | 4 | 5 | 20 | 4 | 16 | 5 | 20 |
| Suitable for data analysis | 5 | 5 | 25 | 5 | 25 | 1 | 5 |
| Room to expand | 3 | 4 | 12 | 5 | 15 | 2 | 6 |
| **Total** |  |  | **123** |  | **108** |  | **77** |

## Decision record
- **Context:** The project needs to analyse structured records and demonstrate anomaly detection within a student project timeframe.
- **Decision:** Use Python as the main technology for the first prototype, with pandas for data handling and scikit-learn for an Isolation Forest experiment. A Flask interface and relational database may be considered as later extensions.
- **Reasons:** Option A has the strongest weighted score, directly supports data analysis and anomaly detection, and keeps the first implementation manageable.
- **Consequences:** The first prototype can demonstrate the core analytical workflow without the extra work of building a complete web application.
- **Risks and next review:** Results depend on the quality and representativeness of the sample data. Review the decision after the first prototype and its tests.
