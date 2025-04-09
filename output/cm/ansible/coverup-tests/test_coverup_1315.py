# file lib/ansible/utils/lock.py:11-43
# lines [36, 37, 39, 40, 41]
# branches ['36->37', '36->39']

import pytest
from unittest.mock import MagicMock
from threading import Lock
from ansible.utils.lock import lock_decorator

class TestClass:
    def __init__(self):
        self._custom_lock = Lock()

    @lock_decorator(attr='_custom_lock')
    def method_with_lock(self):
        return True

def test_lock_decorator_with_attr():
    instance = TestClass()
    assert instance.method_with_lock() == True

    # Ensure that the lock is not acquired after the method_with_lock execution
    assert instance._custom_lock.acquire(blocking=False), "Lock was not released after method_with_lock execution"

    # Clean up by releasing the lock
    instance._custom_lock.release()
