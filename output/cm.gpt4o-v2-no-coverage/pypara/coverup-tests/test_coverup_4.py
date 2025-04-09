# file: pypara/dcc.py:30-39
# asked: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}
# gained: {"lines": [30, 38, 39], "branches": [[38, 0], [38, 39]]}

import pytest
import datetime
from pypara.dcc import _get_date_range
from pypara.commons.zeitgeist import Date

def test_get_date_range():
    start = Date(2023, 1, 1)
    end = Date(2023, 1, 5)
    expected_dates = [
        Date(2023, 1, 1),
        Date(2023, 1, 2),
        Date(2023, 1, 3),
        Date(2023, 1, 4)
    ]
    result = list(_get_date_range(start, end))
    assert result == expected_dates

def test_get_date_range_empty():
    start = Date(2023, 1, 1)
    end = Date(2023, 1, 1)
    result = list(_get_date_range(start, end))
    assert result == []

def test_get_date_range_single_day():
    start = Date(2023, 1, 1)
    end = Date(2023, 1, 2)
    expected_dates = [Date(2023, 1, 1)]
    result = list(_get_date_range(start, end))
    assert result == expected_dates
