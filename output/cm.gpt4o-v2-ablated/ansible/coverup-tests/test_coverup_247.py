# file: lib/ansible/galaxy/api.py:48-53
# asked: {"lines": [48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 53], "branches": []}

import pytest
from unittest.mock import Mock, patch
from threading import Lock

# Assuming _CACHE_LOCK is a global variable in the module
_CACHE_LOCK = Lock()

# Import the cache_lock decorator from the module
from ansible.galaxy.api import cache_lock

def test_cache_lock_decorator():
    mock_func = Mock(return_value="expected_result")

    @cache_lock
    def test_func():
        return mock_func()

    with patch('ansible.galaxy.api._CACHE_LOCK', _CACHE_LOCK):
        result = test_func()

    mock_func.assert_called_once()
    assert result == "expected_result"

    # Ensure the lock was acquired and released
    assert not _CACHE_LOCK.locked()
