# file: pypara/dcc.py:42-55
# asked: {"lines": [42, 55], "branches": []}
# gained: {"lines": [42, 55], "branches": []}

import pytest
from datetime import date
from pypara.dcc import _get_actual_day_count

def test_get_actual_day_count_same_day():
    start = date(2017, 1, 1)
    end = date(2017, 1, 1)
    assert _get_actual_day_count(start, end) == 0

def test_get_actual_day_count_one_day():
    start = date(2017, 1, 1)
    end = date(2017, 1, 2)
    assert _get_actual_day_count(start, end) == 1

def test_get_actual_day_count_multiple_days():
    start = date(2017, 1, 1)
    end = date(2017, 1, 10)
    assert _get_actual_day_count(start, end) == 9

def test_get_actual_day_count_end_before_start():
    start = date(2017, 1, 10)
    end = date(2017, 1, 1)
    assert _get_actual_day_count(start, end) == -9
