# file: pypara/dcc.py:79-83
# asked: {"lines": [79, 83], "branches": []}
# gained: {"lines": [79, 83], "branches": []}

import pytest
import calendar
from pypara.dcc import _is_last_day_of_month
from pypara.commons.zeitgeist import Date

def test_is_last_day_of_month():
    # Test for a date that is the last day of the month
    date = Date(year=2023, month=1, day=31)
    assert _is_last_day_of_month(date) == True

    # Test for a date that is not the last day of the month
    date = Date(year=2023, month=1, day=30)
    assert _is_last_day_of_month(date) == False

    # Test for a leap year date that is the last day of the month
    date = Date(year=2024, month=2, day=29)
    assert _is_last_day_of_month(date) == True

    # Test for a non-leap year date that is the last day of the month
    date = Date(year=2023, month=2, day=28)
    assert _is_last_day_of_month(date) == True

    # Test for a non-leap year date that is not the last day of the month
    date = Date(year=2023, month=2, day=27)
    assert _is_last_day_of_month(date) == False
