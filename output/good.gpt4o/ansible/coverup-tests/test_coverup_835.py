# file lib/ansible/plugins/filter/core.py:87-88
# lines [87, 88]
# branches []

import pytest
from ansible.plugins.filter.core import to_datetime
import datetime

def test_to_datetime():
    # Test with default format
    date_str = "2023-10-01 12:30:45"
    expected_date = datetime.datetime(2023, 10, 1, 12, 30, 45)
    assert to_datetime(date_str) == expected_date

    # Test with custom format
    date_str_custom = "01-10-2023 12:30:45"
    custom_format = "%d-%m-%Y %H:%M:%S"
    expected_date_custom = datetime.datetime(2023, 10, 1, 12, 30, 45)
    assert to_datetime(date_str_custom, custom_format) == expected_date_custom

    # Test with invalid date string
    invalid_date_str = "invalid date"
    with pytest.raises(ValueError):
        to_datetime(invalid_date_str)

    # Test with invalid format
    invalid_format = "%Y/%m/%d"
    with pytest.raises(ValueError):
        to_datetime(date_str, invalid_format)
