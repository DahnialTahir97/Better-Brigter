# Requirements

## Functional requirements (what the system must DO)
1. FR1: The system shall allow authorised users to upload electricity utility records in CSV format.
2. FR2: The system shall validate uploaded records and identify missing values, duplicate entries, and invalid data formats.
3. FR3: The system shall use the Isolation Forest algorithm to identify unusual records based on selected data attributes.
4. FR4: The system shall display flagged records and their anomaly status in a results table.
5. FR5: The system shall allow users to export flagged records for further investigation.

## Non-functional requirements (how the system must PERFORM)

1. NFR1: The system shall process uploaded CSV files within 10 seconds for files containing up to 1,000 records.
2. NFR2: The system shall restrict access to authorised users only.
3. NFR3: The system shall display results in a clear and understandable format.
