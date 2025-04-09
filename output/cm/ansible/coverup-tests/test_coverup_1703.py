# file lib/ansible/utils/lock.py:11-43
# lines [39]
# branches ['36->39']

import pytest
import threading
from functools import wraps
from unittest.mock import MagicMock

# Assuming the lock_decorator is part of the module ansible.utils.lock
from ansible.utils.lock import lock_decorator

class TestClass:
    def __init__(self):
        self._test_lock = threading.Lock()

    @lock_decorator(attr='_test_lock')
    def locked_method(self):
        return "method executed"

def test_lock_decorator_with_lock():
    test_instance = TestClass()
    mock_lock = MagicMock()

    # Patch the __enter__ and __exit__ methods to simulate context manager behavior
    mock_lock.__enter__ = MagicMock()
    mock_lock.__exit__ = MagicMock()

    # Create a new decorator with the mock lock
    decorated_method = lock_decorator(lock=mock_lock)(test_instance.locked_method)

    # Execute the decorated method
    result = decorated_method()

    # Assert that the mock lock was used as a context manager
    mock_lock.__enter__.assert_called_once()
    mock_lock.__exit__.assert_called_once()

    # Assert that the method was executed and returned the correct value
    assert result == "method executed"

    # Clean up by removing the mock lock
    del mock_lock
