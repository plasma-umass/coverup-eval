# file: lib/ansible/plugins/filter/core.py:91-98
# asked: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}
# gained: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime
import time

def test_strftime_with_valid_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    second = 1609459200  # Corresponds to 2021-01-01 00:00:00
    expected_output = "2021-01-01 00:00:00"
    assert strftime(string_format, second) == expected_output

def test_strftime_with_invalid_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    second = "invalid_epoch"
    with pytest.raises(AnsibleFilterError) as excinfo:
        strftime(string_format, second)
    assert "Invalid value for epoch value" in str(excinfo.value)

def test_strftime_without_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    current_time = time.strftime(string_format, time.localtime())
    assert strftime(string_format) == current_time
