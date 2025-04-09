# file pypara/dcc.py:79-83
# lines [79, 83]
# branches []

import pytest
from datetime import date as Date
import calendar
from pypara.dcc import _is_last_day_of_month

def test_is_last_day_of_month():
    # Test for a date that is the last day of the month
    last_day = Date(2023, 1, 31)
    assert _is_last_day_of_month(last_day) == True

    # Test for a date that is not the last day of the month
    not_last_day = Date(2023, 1, 30)
    assert _is_last_day_of_month(not_last_day) == False

    # Test for a leap year, last day of February
    leap_year_last_day = Date(2024, 2, 29)
    assert _is_last_day_of_month(leap_year_last_day) == True

    # Test for a non-leap year, last day of February
    non_leap_year_last_day = Date(2023, 2, 28)
    assert _is_last_day_of_month(non_leap_year_last_day) == True

    # Test for a non-leap year, not the last day of February
    non_leap_year_not_last_day = Date(2023, 2, 27)
    assert _is_last_day_of_month(non_leap_year_not_last_day) == False

    # Test for a month with 30 days, last day
    month_30_days_last_day = Date(2023, 4, 30)
    assert _is_last_day_of_month(month_30_days_last_day) == True

    # Test for a month with 30 days, not the last day
    month_30_days_not_last_day = Date(2023, 4, 29)
    assert _is_last_day_of_month(month_30_days_not_last_day) == False
