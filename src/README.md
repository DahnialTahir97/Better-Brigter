# Source Code

This folder contains the Better-Brighter demonstration code.

- `validation.py` — basic record-level data-quality checks.
- `anomaly_detection.py` — Isolation Forest example for numerical meter readings.
- `sample_data.py` — synthetic demonstration records.
- `main.py` — runs the demonstration and prints a summary.

The code is an academic prototype. It does not connect to a live utility database, alter original meter readings or make billing decisions.

## Run locally

From the repository root:

```bash
pip install -r requirements.txt
python src/main.py
```
