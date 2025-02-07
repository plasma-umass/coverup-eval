# file: tornado/locks.py:446-452
# asked: {"lines": [446, 452], "branches": []}
# gained: {"lines": [446, 452], "branches": []}

import pytest
from unittest.mock import Mock
from tornado.locks import Semaphore

def test_semaphore_exit():
    sem = Semaphore(1)
    
    # Mock the __enter__ method to track its calls
    original_enter = sem.__enter__
    sem.__enter__ = Mock()

    try:
        sem.__exit__(None, None, None)
    except RuntimeError:
        pass

    # Ensure __enter__ was called during __exit__
    sem.__enter__.assert_called_once()

    # Restore the original __enter__ method
    sem.__enter__ = original_enter
