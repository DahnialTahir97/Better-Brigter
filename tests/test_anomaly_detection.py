import pytest

from anomaly_detection import flag_unusual_readings


def test_anomaly_detector_returns_one_flag_per_reading():
    flags = flag_unusual_readings([10, 11, 9, 10, 12, 1000], contamination=0.17)
    assert len(flags) == 6
    assert all(isinstance(flag, bool) for flag in flags)


def test_anomaly_detector_requires_at_least_two_readings():
    with pytest.raises(ValueError):
        flag_unusual_readings([10])
