"""Isolation Forest demonstration for numerical meter readings."""

from sklearn.ensemble import IsolationForest


def flag_unusual_readings(readings, contamination=0.1, random_state=42):
    """Return boolean flags aligned to readings; True means unusual.

    This is an exploratory demonstration, not proof that a record is wrong.
    At least two numeric readings are required by Isolation Forest.
    """
    values = [[float(value)] for value in readings]
    if len(values) < 2:
        raise ValueError("At least two readings are required.")

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
    )
    predictions = model.fit_predict(values)
    return [prediction == -1 for prediction in predictions]
