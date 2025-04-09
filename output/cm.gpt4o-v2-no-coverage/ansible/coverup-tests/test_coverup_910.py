# file: lib/ansible/plugins/filter/core.py:87-88
# asked: {"lines": [87, 88], "branches": []}
# gained: {"lines": [87, 88], "branches": []}

import pytest
import datetime
from ansible.plugins.filter.core import to_datetime

def test_to_datetime_default_format():
    date_str = "2023-10-01 12:30:45"
    expected_date = datetime.datetime(2023, 10, 1, 12, 30, 45)
    result = to_datetime(date_str)
    assert result == expected_date

def test_to_datetime_custom_format():
    date_str = "01-10-2023 12:30:45"
    date_format = "%d-%m-%Y %H:%M:%S"
    expected_date = datetime.datetime(2023, 10, 1, 12, 30, 45)
    result = to_datetime(date_str, date_format)
    assert result == expected_date

def test_to_datetime_invalid_format():
    date_str = "2023/10/01 12:30:45"
    with pytest.raises(ValueError):
        to_datetime(date_str)
