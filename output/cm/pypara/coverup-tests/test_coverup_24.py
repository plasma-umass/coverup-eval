# file pypara/dcc.py:58-76
# lines [58, 63, 66, 68, 71, 73, 76]
# branches ['66->68', '66->76', '71->66', '71->73']

import datetime
import calendar
import pytest
from pypara.dcc import _has_leap_day

@pytest.fixture
def mock_date(monkeypatch):
    class MockDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2020, 2, 29)

    monkeypatch.setattr(datetime, 'date', MockDate)

def test_has_leap_day_with_leap_year(mock_date):
    start = datetime.date(2020, 1, 1)
    end = datetime.date(2020, 12, 31)
    assert _has_leap_day(start, end) is True

def test_has_leap_day_without_leap_year(mock_date):
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 31)
    assert _has_leap_day(start, end) is False

def test_has_leap_day_with_leap_day_at_start(mock_date):
    start = datetime.date(2020, 2, 29)
    end = datetime.date(2020, 3, 1)
    assert _has_leap_day(start, end) is True

def test_has_leap_day_with_leap_day_at_end(mock_date):
    start = datetime.date(2020, 2, 28)
    end = datetime.date(2020, 2, 29)
    assert _has_leap_day(start, end) is True

def test_has_leap_day_with_leap_day_out_of_range(mock_date):
    start = datetime.date(2020, 3, 1)
    end = datetime.date(2021, 2, 28)
    assert _has_leap_day(start, end) is False

def test_has_leap_day_with_range_before_leap_year(mock_date):
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 31)
    assert _has_leap_day(start, end) is False

def test_has_leap_day_with_range_after_leap_year(mock_date):
    start = datetime.date(2021, 1, 1)
    end = datetime.date(2021, 12, 31)
    assert _has_leap_day(start, end) is False

def test_has_leap_day_with_range_spanning_multiple_years_including_leap_year(mock_date):
    start = datetime.date(2019, 1, 1)
    end = datetime.date(2021, 12, 31)
    assert _has_leap_day(start, end) is True
