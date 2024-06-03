# file pypara/dcc.py:176-188
# lines [176, 180, 181, 182, 183, 184, 185, 186, 188]
# branches ['180->181', '180->182', '185->186', '185->188']

import pytest
from datetime import date as Date
import datetime

# Assuming the function _construct_date is imported from pypara.dcc
from pypara.dcc import _construct_date

def test_construct_date_valid():
    # Test with valid date
    result = _construct_date(2023, 10, 5)
    assert result == Date(2023, 10, 5)

def test_construct_date_invalid_year():
    # Test with invalid year
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(0, 10, 5)

def test_construct_date_invalid_month():
    # Test with invalid month
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(2023, 0, 5)

def test_construct_date_invalid_day():
    # Test with invalid day
    with pytest.raises(ValueError, match="year, month and day must be greater than 0."):
        _construct_date(2023, 10, 0)

def test_construct_date_day_out_of_range(mocker):
    # Test with day out of range for month
    mocker.patch('pypara.dcc._construct_date', side_effect=_construct_date)
    result = _construct_date(2023, 2, 30)
    assert result == Date(2023, 2, 28)

def test_construct_date_invalid_date():
    # Test with invalid date that cannot be corrected
    with pytest.raises(ValueError, match="month must be in 1..12"):
        _construct_date(2023, 13, 5)
