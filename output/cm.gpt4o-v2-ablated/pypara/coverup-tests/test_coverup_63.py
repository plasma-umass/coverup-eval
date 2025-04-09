# file: pypara/dcc.py:149-173
# asked: {"lines": [160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}
# gained: {"lines": [160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}

import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
import pytest

# Assuming the function _next_payment_date is defined in pypara/dcc.py
from pypara.dcc import _next_payment_date

def test_next_payment_date_no_eom():
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    expected_date = datetime.date(2015, 1, 1)
    result = _next_payment_date(start_date, frequency)
    assert result == expected_date

def test_next_payment_date_with_eom():
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    eom = 15
    expected_date = datetime.date(2015, 1, 15)
    result = _next_payment_date(start_date, frequency, eom)
    assert result == expected_date

def test_next_payment_date_with_eom_invalid_day():
    start_date = datetime.date(2014, 1, 31)
    frequency = 1
    eom = 31
    expected_date = datetime.date(2015, 1, 31)
    result = _next_payment_date(start_date, frequency, eom)
    assert result == expected_date

def test_next_payment_date_with_decimal_frequency():
    start_date = datetime.date(2014, 1, 1)
    frequency = Decimal('1')
    expected_date = datetime.date(2015, 1, 1)
    result = _next_payment_date(start_date, frequency)
    assert result == expected_date

def test_next_payment_date_with_invalid_eom():
    start_date = datetime.date(2014, 1, 1)
    frequency = 1
    eom = 32  # Invalid day
    expected_date = datetime.date(2015, 1, 1)
    result = _next_payment_date(start_date, frequency, eom)
    assert result == expected_date

@pytest.fixture(autouse=True)
def clean_up(monkeypatch):
    # Use monkeypatch to clean up any state if necessary
    yield
    # Clean up code here if needed

