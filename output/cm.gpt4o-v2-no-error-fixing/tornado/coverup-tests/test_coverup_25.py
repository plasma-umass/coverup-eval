# file: tornado/locks.py:398-413
# asked: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}
# gained: {"lines": [398], "branches": []}

import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
from collections import deque

@pytest.mark.gen_test
async def test_semaphore_release():
    sem = Semaphore(0)
    waiter = Future()
    sem._waiters.append(waiter)
    
    # Ensure the waiter is not done
    assert not waiter.done()
    
    sem.release()
    
    # Check that the semaphore's value is incremented
    assert sem._value == 0
    
    # Check that the waiter is set with the correct result
    assert waiter.done()
    assert isinstance(waiter.result(), _ReleasingContextManager)
    assert waiter.result()._semaphore is sem

@pytest.mark.gen_test
async def test_semaphore_release_no_waiters():
    sem = Semaphore(0)
    
    sem.release()
    
    # Check that the semaphore's value is incremented
    assert sem._value == 1
