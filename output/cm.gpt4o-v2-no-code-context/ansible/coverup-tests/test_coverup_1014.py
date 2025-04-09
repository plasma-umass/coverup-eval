# file: lib/ansible/utils/lock.py:11-43
# asked: {"lines": [36, 37, 39, 40, 41], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [36, 37, 39, 40, 41], "branches": [[36, 37], [36, 39]]}

import threading
import pytest
from unittest.mock import MagicMock

# Assuming the lock_decorator function is defined in ansible.utils.lock
from ansible.utils.lock import lock_decorator

class TestLockDecorator:
    
    def test_lock_decorator_with_attr(self):
        class TestClass:
            def __init__(self):
                self._callback_lock = threading.Lock()
            
            @lock_decorator(attr='_callback_lock')
            def method(self):
                return "locked"
        
        obj = TestClass()
        result = obj.method()
        assert result == "locked"
    
    def test_lock_decorator_with_explicit_lock(self):
        lock = threading.Lock()
        
        @lock_decorator(lock=lock)
        def method():
            return "locked"
        
        result = method()
        assert result == "locked"
    
    def test_lock_decorator_with_missing_attr(self):
        class TestClass:
            def __init__(self):
                self.missing_lock_attr = threading.Lock()
            
            @lock_decorator(attr='missing_lock_attr')
            def method(self):
                return "locked"
        
        obj = TestClass()
        result = obj.method()
        assert result == "locked"
    
    def test_lock_decorator_with_mock_lock(self, mocker):
        mock_lock = mocker.MagicMock()
        
        @lock_decorator(lock=mock_lock)
        def method():
            return "locked"
        
        result = method()
        assert result == "locked"
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()

    def test_lock_decorator_with_attr_and_mock_lock(self, mocker):
        class TestClass:
            def __init__(self):
                self._callback_lock = mocker.MagicMock()
            
            @lock_decorator(attr='_callback_lock')
            def method(self):
                return "locked"
        
        obj = TestClass()
        result = obj.method()
        assert result == "locked"
        obj._callback_lock.__enter__.assert_called_once()
        obj._callback_lock.__exit__.assert_called_once()
