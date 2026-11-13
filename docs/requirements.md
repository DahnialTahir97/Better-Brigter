# Requirements

These requirements describe the intended prototype. They will be refined as the design and implementation progress.

## Functional requirements

1. **FR-01 — Import sample records:** The system shall accept a structured sample dataset of electricity utility records.
2. **FR-02 — Check required fields:** The system shall identify records with missing mandatory values.
3. **FR-03 — Check duplicates:** The system shall identify duplicate record identifiers according to the project's defined rule.
4. **FR-04 — Check data consistency:** The system shall identify invalid data formats and reading values that violate configured validation rules.
5. **FR-05 — Detect unusual records:** The system shall apply an anomaly-detection method to suitable numerical fields and flag records for review.
6. **FR-06 — Present findings:** The system shall provide a summary of flagged records and the reasons they were flagged.
7. **FR-07 — Preserve source data:** The prototype shall retain the original input values and shall not automatically modify meter readings.

## Non-functional requirements

1. **NFR-01 — Usability:** A user shall be able to understand the validation summary and flagged-record reasons without needing to inspect the source code.
2. **NFR-02 — Performance:** The prototype should process a small demonstration dataset of up to 1,000 records within 10 seconds on a typical student laptop; this target must be measured during testing.
3. **NFR-03 — Privacy:** Development and demonstration shall use synthetic or publicly shareable sample data, not confidential live utility records.
4. **NFR-04 — Maintainability:** Validation rules and anomaly-detection logic shall be separated into readable, testable functions.
5. **NFR-05 — Reliability:** The system shall report validation findings consistently for the same input and configuration.

## Acceptance notes

- Each functional requirement should be linked to at least one test or demonstration.
- An anomaly flag indicates an unusual pattern for investigation; it does not prove that the source record is wrong.
- The prototype is an academic demonstration and is not intended for live billing or production operations.
