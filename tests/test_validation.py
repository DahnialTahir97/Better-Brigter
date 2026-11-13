from validation import validate_records


def valid_record(record_id="R001", reading=120.0):
    return {
        "record_id": record_id,
        "meter_id": "M1001",
        "reading_date": "2026-10-01",
        "reading": reading,
    }


def test_valid_record_has_no_issues():
    assert validate_records([valid_record()]) == []


def test_missing_required_field_is_flagged():
    record = valid_record()
    record["meter_id"] = ""
    assert any(
        issue["issue"] == "missing_required_field" and issue["field"] == "meter_id"
        for issue in validate_records([record])
    )


def test_duplicate_record_ids_are_flagged():
    issues = validate_records([valid_record(), valid_record()])
    assert sum(issue["issue"] == "duplicate_record_id" for issue in issues) == 2


def test_non_numeric_reading_is_flagged():
    issues = validate_records([valid_record(reading="not-a-number")])
    assert any(issue["issue"] == "invalid_reading" for issue in issues)


def test_negative_reading_is_flagged():
    issues = validate_records([valid_record(reading=-5)])
    assert any(issue["issue"] == "invalid_reading" for issue in issues)


def test_original_records_are_not_modified():
    record = valid_record()
    before = record.copy()
    validate_records([record])
    assert record == before
