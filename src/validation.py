"""Basic data-quality checks for synthetic electricity utility records."""

from collections import Counter

REQUIRED_FIELDS = ("record_id", "meter_id", "reading_date", "reading")


def validate_records(records):
    """Return a list of issue dictionaries without changing input records."""
    issues = []
    counts = Counter(
        record.get("record_id")
        for record in records
        if record.get("record_id") not in (None, "")
    )

    for index, record in enumerate(records):
        for field in REQUIRED_FIELDS:
            if record.get(field) in (None, ""):
                issues.append({
                    "row": index,
                    "record_id": record.get("record_id"),
                    "issue": "missing_required_field",
                    "field": field,
                })

        record_id = record.get("record_id")
        if record_id not in (None, "") and counts[record_id] > 1:
            issues.append({
                "row": index,
                "record_id": record_id,
                "issue": "duplicate_record_id",
                "field": "record_id",
            })

        reading = record.get("reading")
        if reading not in (None, ""):
            try:
                numeric_reading = float(reading)
                if numeric_reading < 0:
                    raise ValueError
            except (TypeError, ValueError):
                issues.append({
                    "row": index,
                    "record_id": record.get("record_id"),
                    "issue": "invalid_reading",
                    "field": "reading",
                })

    return issues
