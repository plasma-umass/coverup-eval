# file: lib/ansible/utils/lock.py:11-43
# asked: {"lines": [36, 37, 39, 40, 41], "branches": [[36, 37], [36, 39]]}
# gained: {"lines": [36, 37, 39, 40, 41], "branches": [[36, 37], [36, 39]]}

import pytest
import threading
from functools import wraps

# Assuming the lock_decorator function is defined in ansible/utils/lock.py
from ansible.utils.lock import lock_decorator

class TestClass:
    def __init__(self):
        self._callback_lock = threading.Lock()
        self.counter = 0

    @lock_decorator(attr='_callback_lock')
    def increment_with_attr_lock(self):
        self.counter += 1

    @lock_decorator(lock=threading.Lock())
    def increment_with_explicit_lock(self):
        self.counter += 1

@pytest.fixture
def test_instance():
    return TestClass()

def test_increment_with_attr_lock(test_instance):
    test_instance.increment_with_attr_lock()
    assert test_instance.counter == 1

def test_increment_with_explicit_lock(test_instance):
    test_instance.increment_with_explicit_lock()
    assert test_instance.counter == 1

def test_lock_decorator_with_attr(monkeypatch):
    class MockLock:
        def __enter__(self):
            pass
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    mock_lock = MockLock()
    instance = TestClass()
    monkeypatch.setattr(instance, '_callback_lock', mock_lock)

    @lock_decorator(attr='_callback_lock')
    def mock_method(self):
        return "locked"

    result = mock_method(instance)
    assert result == "locked"

def test_lock_decorator_with_explicit_lock():
    class MockLock:
        def __enter__(self):
            pass
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    mock_lock = MockLock()

    @lock_decorator(lock=mock_lock)
    def mock_method():
        return "locked"

    result = mock_method()
    assert result == "locked"
