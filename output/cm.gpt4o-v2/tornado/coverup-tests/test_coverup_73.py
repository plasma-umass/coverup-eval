# file: tornado/locks.py:262-283
# asked: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}
# gained: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}

import pytest
from unittest.mock import Mock

from tornado.locks import _ReleasingContextManager

class MockLock:
    def __init__(self):
        self.released = False

    def release(self):
        self.released = True

def test_releasing_context_manager_init():
    mock_lock = MockLock()
    manager = _ReleasingContextManager(mock_lock)
    assert manager._obj is mock_lock

def test_releasing_context_manager_enter():
    mock_lock = MockLock()
    manager = _ReleasingContextManager(mock_lock)
    assert manager.__enter__() is None

def test_releasing_context_manager_exit():
    mock_lock = MockLock()
    manager = _ReleasingContextManager(mock_lock)
    manager.__exit__(None, None, None)
    assert mock_lock.released

@pytest.fixture
def mock_lock():
    return MockLock()

def test_releasing_context_manager_with_statement(mock_lock):
    manager = _ReleasingContextManager(mock_lock)
    with manager:
        pass
    assert mock_lock.released
