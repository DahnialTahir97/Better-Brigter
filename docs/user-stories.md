# User Stories

As a data quality officer, I want to upload electricity utility records in CSV format, so that I can analyse the records efficiently.

Acceptance criteria:
- The system allows users to upload CSV files.
- The system displays the uploaded file successfully.
Related requirement: FR1

As a data quality officer, I want the system to validate electricity utility records, so that I can identify missing values, duplicate entries and invalid data formats.

Acceptance criteria:
- The system identifies missing values and duplicate entries.
- The system flags records with invalid data formats.
Related requirement: FR2

As a data quality officer, I want the system to detect unusual electricity meter readings, so that I can investigate potential data anomalies.

Acceptance criteria:
- The system uses Isolation Forest to identify unusual records.
- The system displays flagged records and their anomaly status.
Related requirement: FR3