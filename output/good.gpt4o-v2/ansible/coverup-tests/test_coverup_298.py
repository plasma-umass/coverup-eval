# file: lib/ansible/utils/lock.py:11-43
# asked: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}

import pytest
import threading
from functools import wraps
from unittest.mock import Mock

# Assuming the lock_decorator is defined in ansible.utils.lock
from ansible.utils.lock import lock_decorator

class TestLockDecorator:
    
    def test_lock_decorator_with_attr(self):
        class TestClass:
            def __init__(self):
                self._callback_lock = threading.Lock()
            
            @lock_decorator(attr='_callback_lock')
            def method(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.method(5)
        assert result == 10

    def test_lock_decorator_with_explicit_lock(self):
        lock = threading.Lock()
        
        class TestClass:
            @lock_decorator(lock=lock)
            def method(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.method(5)
        assert result == 10

    def test_lock_decorator_with_mock_lock(self, mocker):
        mock_lock = mocker.Mock()
        mock_lock.__enter__ = Mock()
        mock_lock.__exit__ = Mock()
        
        class TestClass:
            @lock_decorator(lock=mock_lock)
            def method(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.method(5)
        assert result == 10
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()

    def test_lock_decorator_with_attr_mock_lock(self, mocker):
        mock_lock = mocker.Mock()
        mock_lock.__enter__ = Mock()
        mock_lock.__exit__ = Mock()
        
        class TestClass:
            def __init__(self):
                self._callback_lock = mock_lock
            
            @lock_decorator(attr='_callback_lock')
            def method(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.method(5)
        assert result == 10
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()
