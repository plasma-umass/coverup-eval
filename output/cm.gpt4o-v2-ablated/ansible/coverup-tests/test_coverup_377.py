# file: lib/ansible/module_utils/api.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest

from ansible.module_utils.api import retry_never

def test_retry_never_with_exception():
    exception = Exception("Test exception")
    result = retry_never(exception)
    assert result is False

def test_retry_never_with_result():
    result = retry_never("Test result")
    assert result is False
