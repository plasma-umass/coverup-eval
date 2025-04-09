# file: lib/ansible/galaxy/api.py:48-53
# asked: {"lines": [48, 49, 50, 51, 53], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 53], "branches": []}

import pytest
import threading
from unittest.mock import Mock

# Assuming the cache_lock decorator and _CACHE_LOCK are defined in the module `ansible.galaxy.api`
from ansible.galaxy.api import cache_lock, _CACHE_LOCK

def test_cache_lock_decorator():
    # Create a mock function to be decorated
    mock_func = Mock()

    # Decorate the mock function with cache_lock
    decorated_func = cache_lock(mock_func)

    # Call the decorated function
    decorated_func()

    # Assert the mock function was called
    mock_func.assert_called_once()

    # Assert the lock was acquired and released
    assert _CACHE_LOCK.locked() is False

def test_cache_lock_with_arguments():
    # Create a mock function to be decorated
    mock_func = Mock()

    # Decorate the mock function with cache_lock
    decorated_func = cache_lock(mock_func)

    # Call the decorated function with arguments
    decorated_func(1, 2, key='value')

    # Assert the mock function was called with the correct arguments
    mock_func.assert_called_once_with(1, 2, key='value')

    # Assert the lock was acquired and released
    assert _CACHE_LOCK.locked() is False
