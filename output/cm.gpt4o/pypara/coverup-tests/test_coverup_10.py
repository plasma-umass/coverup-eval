# file pypara/dcc.py:58-76
# lines [58, 63, 66, 68, 71, 73, 76]
# branches ['66->68', '66->76', '71->66', '71->73']

import pytest
from datetime import date
import calendar
from pypara.dcc import _has_leap_day

def test_has_leap_day():
    # Test case where the range includes a leap day
    start = date(2020, 2, 28)
    end = date(2020, 3, 1)
    assert _has_leap_day(start, end) == True

    # Test case where the range does not include a leap day
    start = date(2019, 2, 28)
    end = date(2019, 3, 1)
    assert _has_leap_day(start, end) == False

    # Test case where the range spans multiple years including a leap year
    start = date(2019, 1, 1)
    end = date(2021, 1, 1)
    assert _has_leap_day(start, end) == True

    # Test case where the range spans multiple years but does not include a leap day
    start = date(2018, 1, 1)
    end = date(2019, 1, 1)
    assert _has_leap_day(start, end) == False

    # Test case where the range is exactly one day on a leap day
    start = date(2020, 2, 29)
    end = date(2020, 2, 29)
    assert _has_leap_day(start, end) == True

    # Test case where the range is exactly one day not on a leap day
    start = date(2021, 2, 28)
    end = date(2021, 2, 28)
    assert _has_leap_day(start, end) == False
