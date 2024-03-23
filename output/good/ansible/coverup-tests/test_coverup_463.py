# file lib/ansible/plugins/filter/core.py:91-98
# lines [91, 93, 94, 95, 96, 97, 98]
# branches ['93->94', '93->98']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime
import time

# Test function to cover the case when second is None
def test_strftime_with_none_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    result = strftime(string_format)
    assert result == time.strftime(string_format, time.localtime())

# Test function to cover the case when second is a valid float
def test_strftime_with_valid_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    second = 1583000000.0  # Example epoch timestamp
    result = strftime(string_format, second)
    assert result == time.strftime(string_format, time.localtime(second))

# Test function to cover the case when second is an invalid value
def test_strftime_with_invalid_second():
    string_format = "%Y-%m-%d %H:%M:%S"
    second = "invalid_epoch"
    with pytest.raises(AnsibleFilterError) as excinfo:
        strftime(string_format, second)
    assert 'Invalid value for epoch value' in str(excinfo.value)
