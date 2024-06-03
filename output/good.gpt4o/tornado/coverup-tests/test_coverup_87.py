# file tornado/locks.py:398-413
# lines [398, 400, 401, 402, 403, 404, 412, 413]
# branches ['401->exit', '401->402', '403->401', '403->404']

import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
from tornado.locks import _ReleasingContextManager

@pytest.fixture
def semaphore():
    return Semaphore(0)

def test_semaphore_release_with_waiters(mocker, semaphore):
    # Mocking a waiter Future
    waiter = Future()
    mocker.patch.object(waiter, 'done', return_value=False)
    mocker.patch.object(waiter, 'set_result')

    # Adding the mocked waiter to the semaphore's waiters
    semaphore._waiters.append(waiter)

    # Initial value should be 0
    assert semaphore._value == 0

    # Release the semaphore, which should decrement the value and set the result for the waiter
    semaphore.release()

    # The value should be decremented back to 0 after being incremented to 1
    assert semaphore._value == 0

    # The waiter's set_result should have been called with _ReleasingContextManager
    waiter.set_result.assert_called_once()
    assert isinstance(waiter.set_result.call_args[0][0], _ReleasingContextManager)

    # Clean up: ensure the waiters list is empty
    assert len(semaphore._waiters) == 0
