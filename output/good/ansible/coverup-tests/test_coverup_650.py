# file lib/ansible/galaxy/api.py:48-53
# lines [48, 49, 50, 51, 53]
# branches []

import pytest
from threading import Lock
from unittest.mock import MagicMock, patch

# Assuming the _CACHE_LOCK is a global variable in the module ansible.galaxy.api
# We will mock this lock for the purpose of the test
from ansible.galaxy.api import cache_lock

# Mock the _CACHE_LOCK for testing purposes
@pytest.fixture
def mock_cache_lock(mocker):
    mocker.patch('ansible.galaxy.api._CACHE_LOCK', new=Lock())

# Test function to ensure the cache_lock decorator acquires the lock
def test_cache_lock_decorator(mock_cache_lock):
    # Create a mock function to wrap
    mock_func = MagicMock(return_value='mocked_result')

    # Wrap the mock function with the cache_lock decorator
    wrapped_func = cache_lock(mock_func)

    # Call the wrapped function
    result = wrapped_func()

    # Assert that the result is as expected
    assert result == 'mocked_result'
    # Assert that the mock function was called once
    mock_func.assert_called_once()
