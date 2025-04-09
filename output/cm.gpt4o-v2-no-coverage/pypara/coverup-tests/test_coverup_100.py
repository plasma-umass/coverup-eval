# file: pypara/dcc.py:79-83
# asked: {"lines": [79, 83], "branches": []}
# gained: {"lines": [79, 83], "branches": []}

import pytest
from datetime import date as Date
from pypara.dcc import _is_last_day_of_month

def test_is_last_day_of_month():
    # Test for a date that is the last day of the month
    assert _is_last_day_of_month(Date(2023, 1, 31)) == True
    assert _is_last_day_of_month(Date(2023, 2, 28)) == True
    assert _is_last_day_of_month(Date(2024, 2, 29)) == True  # Leap year
    assert _is_last_day_of_month(Date(2023, 4, 30)) == True

    # Test for a date that is not the last day of the month
    assert _is_last_day_of_month(Date(2023, 1, 30)) == False
    assert _is_last_day_of_month(Date(2023, 2, 27)) == False
    assert _is_last_day_of_month(Date(2023, 4, 29)) == False

    # Test for the first day of the month
    assert _is_last_day_of_month(Date(2023, 1, 1)) == False
    assert _is_last_day_of_month(Date(2023, 2, 1)) == False
    assert _is_last_day_of_month(Date(2023, 4, 1)) == False
