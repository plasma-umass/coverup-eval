# file: lib/ansible/utils/lock.py:11-43
# asked: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [11, 31, 32, 33, 36, 37, 39, 40, 41, 42, 43], "branches": [[36, 37], [36, 39]]}

import threading
import pytest
from functools import wraps

# Assuming the lock_decorator function is defined in ansible/utils/lock.py
from ansible.utils.lock import lock_decorator

class TestLockDecorator:
    
    def test_lock_decorator_with_attr(self):
        class TestClass:
            def __init__(self):
                self._callback_lock = threading.Lock()
            
            @lock_decorator(attr='_callback_lock')
            def critical_section(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.critical_section(5)
        assert result == 10

    def test_lock_decorator_with_explicit_lock(self):
        lock = threading.Lock()
        
        class TestClass:
            @lock_decorator(lock=lock)
            def critical_section(self, x):
                return x * 2
        
        obj = TestClass()
        result = obj.critical_section(5)
        assert result == 10

    def test_lock_decorator_without_lock(self):
        class TestClass:
            @lock_decorator()
            def critical_section(self, x):
                return x * 2
        
        obj = TestClass()
        with pytest.raises(AttributeError):
            obj.critical_section(5)
