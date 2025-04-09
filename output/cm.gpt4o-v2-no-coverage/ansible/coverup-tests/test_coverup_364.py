# file: lib/ansible/utils/lock.py:11-43
# asked: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}

import threading
import pytest
from functools import wraps
from unittest.mock import Mock

# Assuming the lock_decorator is defined in ansible/utils/lock.py
from ansible.utils.lock import lock_decorator

class TestLockDecorator:
    
    def test_lock_decorator_with_attr(self):
        class TestClass:
            def __init__(self):
                self._callback_lock = threading.Lock()
                self.counter = 0

            @lock_decorator(attr='_callback_lock')
            def increment(self):
                self.counter += 1

        obj = TestClass()
        obj.increment()
        assert obj.counter == 1

    def test_lock_decorator_with_lock(self):
        class TestClass:
            def __init__(self):
                self.counter = 0

            @lock_decorator(lock=threading.Lock())
            def increment(self):
                self.counter += 1

        obj = TestClass()
        obj.increment()
        assert obj.counter == 1

    def test_lock_decorator_with_mock_lock(self, mocker):
        mock_lock = mocker.Mock()
        mock_lock.__enter__ = Mock()
        mock_lock.__exit__ = Mock()

        class TestClass:
            def __init__(self):
                self.counter = 0

            @lock_decorator(lock=mock_lock)
            def increment(self):
                self.counter += 1

        obj = TestClass()
        obj.increment()
        assert obj.counter == 1
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()

    def test_lock_decorator_with_missing_attr(self):
        class TestClass:
            def __init__(self):
                self.counter = 0

            @lock_decorator(attr='non_existent_lock')
            def increment(self):
                self.counter += 1

        obj = TestClass()
        with pytest.raises(AttributeError):
            obj.increment()
