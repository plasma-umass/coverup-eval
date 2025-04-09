# file: pypara/dcc.py:149-173
# asked: {"lines": [149, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}
# gained: {"lines": [149, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}

import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
import pytest
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

def test_next_payment_date_with_invalid_eom():
    start_date = datetime.date(2014, 1, 31)
    frequency = 1
    eom = 30
    expected_date = datetime.date(2015, 1, 30)  # Should adjust to the 30th of the month
    result = _next_payment_date(start_date, frequency, eom)
    assert result == expected_date

@pytest.mark.parametrize("start_date, frequency, eom, expected_date", [
    (datetime.date(2014, 1, 1), 1, None, datetime.date(2015, 1, 1)),
    (datetime.date(2014, 1, 1), 1, 15, datetime.date(2015, 1, 15)),
    (datetime.date(2014, 1, 31), 1, 30, datetime.date(2015, 1, 30)),
    (datetime.date(2014, 2, 28), 1, 31, datetime.date(2015, 2, 28)),
])
def test_next_payment_date_parametrized(start_date, frequency, eom, expected_date):
    result = _next_payment_date(start_date, frequency, eom)
    assert result == expected_date
