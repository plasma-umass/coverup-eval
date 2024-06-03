# file lib/ansible/plugins/filter/core.py:91-98
# lines [91, 93, 94, 95, 96, 97, 98]
# branches ['93->94', '93->98']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime
import time

def test_strftime_with_valid_second():
    # Test with a valid second value
    result = strftime('%Y-%m-%d %H:%M:%S', 1609459200)  # 2021-01-01 00:00:00
    assert result == '2021-01-01 00:00:00'

def test_strftime_with_invalid_second():
    # Test with an invalid second value
    with pytest.raises(AnsibleFilterError, match='Invalid value for epoch value'):
        strftime('%Y-%m-%d %H:%M:%S', 'invalid')

def test_strftime_with_none_second():
    # Test with second as None
    result = strftime('%Y-%m-%d %H:%M:%S')
    assert result == time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def test_strftime_with_float_second():
    # Test with a float second value
    result = strftime('%Y-%m-%d %H:%M:%S', 1609459200.0)  # 2021-01-01 00:00:00
    assert result == '2021-01-01 00:00:00'
