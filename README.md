# Better-Brigter
Electricity Utility Records
Problem Statement

Who is affected?
[Electricity utility data quality officers, data analysts, and electricity utility organisations that manage meter readings and customer electricity records]

What exactly is going wrong?
[Electricity utility records may contain missing values, duplicate entries, inconsistent data, or unusual meter readings. These issues can make it difficult to identify records that require further investigation.]

Why does it matter?
[Poor data quality may affect the accuracy of reports, increase manual checking workload, and delay the identification of potential data errors.]
Problem statement (3 to 5 sentences)

[Electricity utility organisations rely on accurate meter readings and customer records to support data analysis and operational decision-making. However, these records may contain missing values, duplicate entries, inconsistent information, or unusual readings that are difficult to identify through manual checking alone. These problems can increase the workload of data quality officers and affect the reliability of reports. Therefore, a machine learning-based anomaly detection system is proposed to identify unusual records and flag them for further investigation by authorised users.]

Requirements
Functional requirements (what the system must DO)
FR1: The system shall allow authorised users to upload electricity utility records in CSV format.
FR2: The system shall validate uploaded records and identify missing values, duplicate entries, and invalid data formats.
FR3: The system shall use the Isolation Forest algorithm to identify unusual records based on selected data attributes.
FR4: The system shall display flagged records and their anomaly status in a results table.
FR5: The system shall allow users to export flagged records and validation results into a downloadable CSV file.
FR6: The system shall display a summary of the total records analysed and the number of records flagged as anomalies.
Non-functional requirements (how the system must PERFORM)
NFR1 — Performance: The system shall process a dataset containing up to 10,000 records within 10 seconds under the defined test environment.
NFR2 — Security: The system shall restrict access to uploaded records and analysis results to authorised users.
NFR3 — Reliability: The system shall display a clear error message when an uploaded file has an unsupported format or contains unreadable data.
NFR4 — Usability: The system shall allow users to upload a valid CSV file and view the analysis results through a graphical interface without requiring them to write code.

User Stories
Format: As a [type of user], I want [goal], so that [reason or benefit].
User Story 1 — Data Quality Officer

As a data quality officer, I want to upload electricity utility records in CSV format, so that I can analyse the records efficiently.

Acceptance Criteria:
1. Given a valid CSV file, when I upload it, then the system shall accept the file and display the uploaded data.
2. Given an unsupported file format, when I upload it, then the system shall reject the file and display an error message.

Related requirements: FR1, NFR3.

--
User Story 2 — Data Analyst

As a data analyst, I want the system to identify unusual electricity utility records, so that I can investigate potential data quality issues.

Acceptance Criteria:
1. Given a valid dataset, when I run the anomaly detection process, then the system shall identify and flag records classified as anomalies by the model.
2. The system shall display the anomaly status for each flagged record.

Related requirements: FR3, FR4.

---

User Story 3 — Data Quality Supervisor

As a data quality supervisor, I want to view summary statistics and export flagged records, so that I can review the findings and prepare reports.

Acceptance Criteria:
1. After analysis, the system shall display the total number of records analysed and the number flagged as anomalies.
2. When I export the results, the system shall generate a downloadable CSV file containing the flagged records and their anomaly status.

Related requirements:FR5, FR6.
