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
    generated_dates = list(_get_date_range(start, end))
    assert generated_dates == expected_dates

    # Test with start date equal to end date
    start = Date(2023, 1, 1)
    end = Date(2023, 1, 1)
    generated_dates = list(_get_date_range(start, end))
    assert generated_dates == []

    # Test with start date after end date
    start = Date(2023, 1, 5)
    end = Date(2023, 1, 1)
    generated_dates = list(_get_date_range(start, end))
    assert generated_dates == []
