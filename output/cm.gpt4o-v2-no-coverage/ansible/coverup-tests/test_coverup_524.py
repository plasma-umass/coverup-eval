# file: lib/ansible/plugins/filter/core.py:91-98
# asked: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}
# gained: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}

import pytest
import time
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime

def test_strftime_no_second():
    format_string = "%Y-%m-%d %H:%M:%S"
    result = strftime(format_string)
    assert isinstance(result, str)
    assert time.strptime(result, format_string)

def test_strftime_with_valid_second():
    format_string = "%Y-%m-%d %H:%M:%S"
    second = 1609459200  # 2021-01-01 00:00:00
    result = strftime(format_string, second)
    assert result == "2021-01-01 00:00:00"

def test_strftime_with_invalid_second():
    format_string = "%Y-%m-%d %H:%M:%S"
    invalid_second = "invalid"
    with pytest.raises(AnsibleFilterError) as excinfo:
        strftime(format_string, invalid_second)
    assert "Invalid value for epoch value" in str(excinfo.value)
