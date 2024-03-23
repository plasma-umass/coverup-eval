# file pypara/dcc.py:176-188
# lines [188]
# branches ['185->188']

import pytest
import datetime
from pypara.dcc import _construct_date

def test_construct_date_day_out_of_range(mocker):
    # Mock datetime.date to raise ValueError for a specific condition
    original_date = datetime.date
    def date_side_effect(year, month, day):
        if day > 28 and month == 2:
            raise ValueError("day is out of range for month")
        return original_date(year, month, day)
    mocker.patch('datetime.date', side_effect=date_side_effect)
    
    # Test with a day out of range for the month
    corrected_date = _construct_date(2021, 2, 29)
    assert corrected_date == original_date(2021, 2, 28), "The date should be corrected to the last valid day of the month"

def test_construct_date_invalid_date(mocker):
    # Mock datetime.date to always raise ValueError
    mocker.patch('datetime.date', side_effect=ValueError("Invalid date"))

    # Test with an invalid date that does not match the specific "day out of range" error
    with pytest.raises(ValueError) as exc_info:
        _construct_date(2021, 2, 30)
    assert str(exc_info.value) == "Invalid date", "A ValueError should be raised for an invalid date"
