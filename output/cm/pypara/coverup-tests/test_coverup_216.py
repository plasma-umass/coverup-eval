# file pypara/dcc.py:79-83
# lines [83]
# branches []

import calendar
from datetime import date
import pytest

# Assuming the Date class is imported from somewhere, if not, using datetime.date for the example
from pypara.dcc import _is_last_day_of_month  # Replace with the correct import if necessary

def test_is_last_day_of_month():
    # Test for the last day of the month
    last_day_date = date(2023, 3, 31)  # March 31, 2023 is the last day of the month
    assert _is_last_day_of_month(last_day_date) is True

    # Test for a day that is not the last day of the month
    not_last_day_date = date(2023, 3, 30)  # March 30, 2023 is not the last day of the month
    assert _is_last_day_of_month(not_last_day_date) is False

    # Test for February in a leap year
    feb_leap_year = date(2024, 2, 29)  # February 29, 2024 is the last day of the month in a leap year
    assert _is_last_day_of_month(feb_leap_year) is True

    # Test for February in a non-leap year
    feb_non_leap_year = date(2023, 2, 28)  # February 28, 2023 is the last day of the month in a non-leap year
    assert _is_last_day_of_month(feb_non_leap_year) is True

# No cleanup is necessary as the test does not modify any state or external resources
