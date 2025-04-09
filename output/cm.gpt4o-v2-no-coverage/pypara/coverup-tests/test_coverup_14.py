# file: pypara/dcc.py:176-188
# asked: {"lines": [176, 180, 181, 182, 183, 184, 185, 186, 188], "branches": [[180, 181], [180, 182], [185, 186], [185, 188]]}
# gained: {"lines": [176, 180, 181, 182, 183, 184, 185, 186, 188], "branches": [[180, 181], [180, 182], [185, 186], [185, 188]]}

import pytest
import datetime
from pypara.dcc import _construct_date

def test_construct_date_valid():
    date = _construct_date(2023, 10, 5)
    assert date == datetime.date(2023, 10, 5)

def test_construct_date_invalid_day():
    date = _construct_date(2023, 2, 30)
    assert date == datetime.date(2023, 2, 28)

def test_construct_date_invalid_month():
    with pytest.raises(ValueError, match="month must be in 1..12"):
        _construct_date(2023, 13, 1)

def test_construct_date_invalid_year():
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(0, 10, 5)

def test_construct_date_negative_day():
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(2023, 10, -5)

def test_construct_date_negative_month():
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(2023, -10, 5)

def test_construct_date_negative_year():
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(-2023, 10, 5)
