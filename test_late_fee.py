import pytest
from late_fee import late_fee


def test_zero_days_returns_zero():
    assert late_fee(0, 10) == 0


def test_calculates_fee_correctly():
    assert late_fee(3, 10) == 30


def test_fee_is_limited_to_100():
    assert late_fee(15, 10) == 100


def test_negative_days_raise_error():
    with pytest.raises(ValueError):
        late_fee(-1, 10)


def test_fractional_days_raise_error():
    with pytest.raises(ValueError):
        late_fee(1.5, 10)


def test_negative_daily_rate_raises_error():
    with pytest.raises(ValueError):
        late_fee(3, -10)
