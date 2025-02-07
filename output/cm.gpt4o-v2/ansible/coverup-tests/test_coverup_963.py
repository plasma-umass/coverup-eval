# file: lib/ansible/module_utils/api.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from ansible.module_utils.api import retry_never

def test_retry_never():
    # Test with an exception
    assert retry_never(Exception("Test exception")) is False

    # Test with a result
    assert retry_never("Test result") is False
