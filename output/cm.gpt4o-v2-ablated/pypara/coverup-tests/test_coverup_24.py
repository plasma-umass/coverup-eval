# file: pypara/dcc.py:42-55
# asked: {"lines": [42, 55], "branches": []}
# gained: {"lines": [42, 55], "branches": []}

import datetime
import pytest
from pypara.dcc import _get_actual_day_count

def test_get_actual_day_count_same_day():
    start = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 1, 1)
    assert _get_actual_day_count(start, end) == 0

def test_get_actual_day_count_one_day():
    start = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 1, 2)
    assert _get_actual_day_count(start, end) == 1

def test_get_actual_day_count_multiple_days():
    start = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 1, 10)
    assert _get_actual_day_count(start, end) == 9

def test_get_actual_day_count_start_after_end():
    start = datetime.date(2017, 1, 10)
    end = datetime.date(2017, 1, 1)
    assert _get_actual_day_count(start, end) == -9

def test_get_actual_day_count_leap_year():
    start = datetime.date(2020, 2, 28)
    end = datetime.date(2020, 3, 1)
    assert _get_actual_day_count(start, end) == 2
