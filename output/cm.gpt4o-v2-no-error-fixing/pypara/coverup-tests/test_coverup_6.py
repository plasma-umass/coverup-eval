# file: pypara/dcc.py:30-39
# asked: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}
# gained: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}

import pytest
from datetime import date, timedelta
from pypara.dcc import _get_date_range

def test_get_date_range():
    start = date(2023, 1, 1)
    end = date(2023, 1, 5)
    expected_dates = [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3), date(2023, 1, 4)]
    
    result = list(_get_date_range(start, end))
    
    assert result == expected_dates

def test_get_date_range_empty():
    start = date(2023, 1, 1)
    end = date(2023, 1, 1)
    
    result = list(_get_date_range(start, end))
    
    assert result == []

def test_get_date_range_single_day():
    start = date(2023, 1, 1)
    end = date(2023, 1, 2)
    expected_dates = [date(2023, 1, 1)]
    
    result = list(_get_date_range(start, end))
    
    assert result == expected_dates
