# file: lib/ansible/plugins/filter/core.py:87-88
# asked: {"lines": [87, 88], "branches": []}
# gained: {"lines": [87, 88], "branches": []}

import pytest
from datetime import datetime
from ansible.plugins.filter.core import to_datetime

def test_to_datetime_default_format():
    test_string = "2023-10-01 12:30:45"
    expected_result = datetime(2023, 10, 1, 12, 30, 45)
    result = to_datetime(test_string)
    assert result == expected_result

def test_to_datetime_custom_format():
    test_string = "01-10-2023 12:30:45"
    custom_format = "%d-%m-%Y %H:%M:%S"
    expected_result = datetime(2023, 10, 1, 12, 30, 45)
    result = to_datetime(test_string, custom_format)
    assert result == expected_result
