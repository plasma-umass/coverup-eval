# file lib/ansible/utils/lock.py:11-43
# lines [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43]
# branches ['36->37', '36->39']

import threading
import pytest
from unittest.mock import MagicMock

# Assuming the lock_decorator function is imported from ansible.utils.lock
from ansible.utils.lock import lock_decorator

class TestClass:
    def __init__(self):
        self._callback_lock = threading.Lock()

    @lock_decorator(attr='_callback_lock')
    def method_with_attr_lock(self):
        return "locked with attr"

    @lock_decorator(lock=threading.Lock())
    def method_with_explicit_lock(self):
        return "locked with explicit lock"

def test_method_with_attr_lock():
    obj = TestClass()
    result = obj.method_with_attr_lock()
    assert result == "locked with attr"

def test_method_with_explicit_lock():
    obj = TestClass()
    result = obj.method_with_explicit_lock()
    assert result == "locked with explicit lock"

def test_lock_decorator_with_mock(mocker):
    mock_lock = mocker.MagicMock()
    mock_lock.__enter__ = MagicMock()
    mock_lock.__exit__ = MagicMock()

    @lock_decorator(lock=mock_lock)
    def mock_method():
        return "mock lock"

    result = mock_method()
    assert result == "mock lock"
    mock_lock.__enter__.assert_called_once()
    mock_lock.__exit__.assert_called_once()

