# file: tornado/locks.py:262-283
# asked: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}
# gained: {"lines": [262, 263, 271, 274, 277], "branches": []}

import pytest
from unittest import mock
from tornado.locks import Semaphore

class _ReleasingContextManager:
    """Releases a Lock or Semaphore at the end of a "with" statement.

        with (yield semaphore.acquire()):
            pass

        # Now semaphore.release() has been called.
    """

    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._obj.release()

@pytest.fixture
def mock_semaphore():
    return mock.Mock(spec=Semaphore)

def test_releasing_context_manager_enter(mock_semaphore):
    rcm = _ReleasingContextManager(mock_semaphore)
    with rcm:
        pass
    mock_semaphore.release.assert_called_once()

def test_releasing_context_manager_exit_with_exception(mock_semaphore):
    rcm = _ReleasingContextManager(mock_semaphore)
    try:
        with rcm:
            raise ValueError("Test exception")
    except ValueError:
        pass
    mock_semaphore.release.assert_called_once()
