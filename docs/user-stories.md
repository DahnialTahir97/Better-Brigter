# User Stories

The following stories describe the needs of the intended users. Acceptance criteria make each story easier to verify.

## US-01 — Check uploaded records
As a data quality officer, I want to provide a sample electricity utility dataset, so that I can run checks on records in one place.

**Acceptance criteria**
- The prototype accepts the agreed structured input format.
- The prototype reports an understandable error when the input cannot be read.

## US-02 — Find incomplete records
As a data quality officer, I want records with missing mandatory fields to be flagged, so that I can review incomplete information.

**Acceptance criteria**
- A record with a missing required value is flagged.
- The result identifies the field or rule that caused the flag.

## US-03 — Identify duplicates
As a data quality officer, I want duplicate record identifiers to be identified, so that repeated entries can be investigated.

**Acceptance criteria**
- Duplicate identifiers are detected using the agreed identifier field.
- The original records remain unchanged.

## US-04 — Detect unusual readings
As a data quality officer, I want unusual meter-reading patterns to be highlighted, so that I can investigate possible data issues.

**Acceptance criteria**
- The prototype applies a documented anomaly-detection method to suitable numerical data.
- Flagged records are presented as candidates for review, not confirmed errors.

## US-05 — Review a summary
As a supervisor, I want to see a summary of validation findings, so that I can understand the types and number of potential issues identified.

**Acceptance criteria**
- The summary reports the total records checked and the number of records flagged.
- Findings are grouped by validation reason where applicable.

## US-06 — Protect original data
As an authorised user, I want the original input records to remain unchanged, so that the prototype does not interfere with source readings or billing decisions.

**Acceptance criteria**
- Validation and anomaly detection produce separate findings.
- The prototype does not overwrite the original input values.
