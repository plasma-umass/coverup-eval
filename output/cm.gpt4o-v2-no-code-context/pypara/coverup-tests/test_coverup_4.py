# file: pypara/dcc.py:30-39
# asked: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}
# gained: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}

import pytest
from datetime import datetime, timedelta
from pypara.dcc import _get_date_range

def test_get_date_range():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 5)
    expected_dates = [
        datetime(2023, 1, 1),
        datetime(2023, 1, 2),
        datetime(2023, 1, 3),
        datetime(2023, 1, 4)
    ]
    
    result = list(_get_date_range(start, end))
    
    assert result == expected_dates

def test_get_date_range_empty():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 1)
    
    result = list(_get_date_range(start, end))
    
    assert result == []

def test_get_date_range_single_day():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)
    expected_dates = [datetime(2023, 1, 1)]
    
    result = list(_get_date_range(start, end))
    
    assert result == expected_dates
