"""Run the Better-Brighter synthetic-data demonstration."""

from anomaly_detection import flag_unusual_readings
from sample_data import SAMPLE_RECORDS
from validation import validate_records


def main():
    print("BETTER-BRIGHTER | Electricity Utility Record Demo")
    print(f"Records checked: {len(SAMPLE_RECORDS)}")

    issues = validate_records(SAMPLE_RECORDS)
    print(f"Data-quality issues: {len(issues)}")
    for issue in issues:
        print(f"- Row {issue['row'] + 1}: {issue['issue']} ({issue['field']})")

    readings = [record["reading"] for record in SAMPLE_RECORDS]
    flags = flag_unusual_readings(readings)
    flagged = [
        record["record_id"]
        for record, is_flagged in zip(SAMPLE_RECORDS, flags)
        if is_flagged
    ]
    print(f"Unusual readings flagged for review: {', '.join(flagged) or 'None'}")
    print("Reminder: flags indicate unusual patterns, not confirmed errors.")


if __name__ == "__main__":
    main()
