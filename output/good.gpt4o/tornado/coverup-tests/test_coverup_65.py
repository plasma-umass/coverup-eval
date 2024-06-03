# file tornado/locks.py:262-283
# lines [262, 263, 271, 272, 274, 275, 277, 283]
# branches []

import pytest
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
def semaphore():
    return Semaphore(1)

def test_releasing_context_manager(semaphore):
    # Acquire the semaphore
    semaphore.acquire()
    assert semaphore._value == 0  # Ensure semaphore is acquired

    # Use the _ReleasingContextManager to release the semaphore
    with _ReleasingContextManager(semaphore):
        pass

    # Ensure semaphore is released
    assert semaphore._value == 1
