# file: pypara/dcc.py:79-83
# asked: {"lines": [79, 83], "branches": []}
# gained: {"lines": [79, 83], "branches": []}

import pytest
from datetime import date as Date
import calendar

# Assuming the function _is_last_day_of_month is part of a class or module, 
# we need to import it. For this example, let's assume it's part of a module named `dcc`.

from pypara.dcc import _is_last_day_of_month

def test_is_last_day_of_month_true():
    # Test a date that is the last day of the month
    test_date = Date(2023, 1, 31)
    assert _is_last_day_of_month(test_date) == True

def test_is_last_day_of_month_false():
    # Test a date that is not the last day of the month
    test_date = Date(2023, 1, 30)
    assert _is_last_day_of_month(test_date) == False

def test_is_last_day_of_february_leap_year():
    # Test the last day of February in a leap year
    test_date = Date(2024, 2, 29)
    assert _is_last_day_of_month(test_date) == True

def test_is_last_day_of_february_non_leap_year():
    # Test the last day of February in a non-leap year
    test_date = Date(2023, 2, 28)
    assert _is_last_day_of_month(test_date) == True

def test_is_not_last_day_of_february_non_leap_year():
    # Test a date in February that is not the last day in a non-leap year
    test_date = Date(2023, 2, 27)
    assert _is_last_day_of_month(test_date) == False
