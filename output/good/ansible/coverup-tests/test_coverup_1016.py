# file lib/ansible/module_utils/api.py:134-135
# lines [134, 135]
# branches []

import pytest
from ansible.module_utils.api import retry_never

def test_retry_never():
    # Test that retry_never always returns False regardless of the input
    assert retry_never(Exception()) is False, "retry_never should return False for exceptions"
    assert retry_never("result") is False, "retry_never should return False for non-exception results"
    assert retry_never(None) is False, "retry_never should return False for None"
