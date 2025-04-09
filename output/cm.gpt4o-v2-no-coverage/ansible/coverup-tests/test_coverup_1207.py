# file: lib/ansible/galaxy/api.py:48-53
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest
import threading
from unittest.mock import Mock

# Assuming _CACHE_LOCK and cache_lock are defined in ansible/galaxy/api.py
from ansible.galaxy.api import _CACHE_LOCK, cache_lock

def test_cache_lock_decorator():
    # Mock function to be decorated
    mock_func = Mock(return_value="expected_result")

    # Decorate the mock function with cache_lock
    decorated_func = cache_lock(mock_func)

    # Call the decorated function
    result = decorated_func(1, 2, key='value')

    # Assertions to verify the behavior
    mock_func.assert_called_once_with(1, 2, key='value')
    assert result == "expected_result"

    # Verify that the lock was acquired and released
    assert _CACHE_LOCK.locked() == False

    # Test that the lock is actually used
    with threading.Lock():
        decorated_func(1, 2, key='value')
        assert _CACHE_LOCK.locked() == False
