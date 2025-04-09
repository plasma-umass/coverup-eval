# file: tornado/locks.py:398-413
# asked: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}
# gained: {"lines": [398], "branches": []}

import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
from collections import deque

@pytest.mark.gen_test
async def test_semaphore_release():
    sem = Semaphore(1)
    waiter = Future()
    sem._waiters.append(waiter)
    
    # Release the semaphore and check the value
    sem.release()
    assert sem._value == 1
    assert waiter.done() == False

    # Simulate a waiter that is not done
    waiter = Future()
    sem._waiters.append(waiter)
    sem.release()
    assert sem._value == 0
    assert waiter.done() == True
    assert isinstance(waiter.result(), _ReleasingContextManager)

    # Clean up
    sem._waiters.clear()
