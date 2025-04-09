# file: pypara/dcc.py:58-76
# asked: {"lines": [58, 63, 66, 68, 71, 73, 76], "branches": [[66, 68], [66, 76], [71, 66], [71, 73]]}
# gained: {"lines": [58, 63, 66, 68, 71, 73, 76], "branches": [[66, 68], [66, 76], [71, 73]]}

import pytest
import datetime
import calendar
from pypara.dcc import _has_leap_day

def test_has_leap_day_with_leap_day():
    start = datetime.date(2020, 1, 1)
    end = datetime.date(2020, 12, 31)
    assert _has_leap_day(start, end) == True

def test_has_leap_day_without_leap_day():
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 31)
    assert _has_leap_day(start, end) == False

def test_has_leap_day_crossing_leap_year():
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2020, 12, 31)
    assert _has_leap_day(start, end) == True

def test_has_leap_day_multiple_leap_years():
    start = datetime.date(2016, 1, 1)
    end = datetime.date(2020, 12, 31)
    assert _has_leap_day(start, end) == True

def test_has_leap_day_no_leap_years():
    start = datetime.date(2018, 1, 1)
    end = datetime.date(2019, 12, 31)
    assert _has_leap_day(start, end) == False
