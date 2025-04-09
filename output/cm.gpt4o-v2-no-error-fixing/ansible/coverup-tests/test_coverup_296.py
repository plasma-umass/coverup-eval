# file: lib/ansible/plugins/filter/core.py:91-98
# asked: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}
# gained: {"lines": [91, 93, 94, 95, 96, 97, 98], "branches": [[93, 94], [93, 98]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import strftime

def test_strftime_with_valid_second():
    result = strftime("%Y-%m-%d %H:%M:%S", 1638316800)
    assert result == "2021-12-01 00:00:00"

def test_strftime_with_invalid_second():
    with pytest.raises(AnsibleFilterError, match="Invalid value for epoch value"):
        strftime("%Y-%m-%d %H:%M:%S", "invalid")

def test_strftime_without_second():
    result = strftime("%Y-%m-%d %H:%M:%S")
    assert isinstance(result, str)
