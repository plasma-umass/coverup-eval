# file: pypara/dcc.py:58-76
# asked: {"lines": [58, 63, 66, 68, 71, 73, 76], "branches": [[66, 68], [66, 76], [71, 66], [71, 73]]}
# gained: {"lines": [58, 63, 66, 68, 71, 73, 76], "branches": [[66, 68], [66, 76], [71, 73]]}

import pytest
from datetime import date as Date
from pypara.dcc import _has_leap_day

def test_has_leap_day_with_leap_day():
    start = Date(2020, 2, 28)
    end = Date(2020, 3, 1)
    assert _has_leap_day(start, end) == True

def test_has_leap_day_without_leap_day():
    start = Date(2019, 2, 28)
    end = Date(2019, 3, 1)
    assert _has_leap_day(start, end) == False

def test_has_leap_day_across_years_with_leap_day():
    start = Date(2019, 1, 1)
    end = Date(2021, 1, 1)
    assert _has_leap_day(start, end) == True

def test_has_leap_day_across_years_without_leap_day():
    start = Date(2018, 1, 1)
    end = Date(2019, 1, 1)
    assert _has_leap_day(start, end) == False
