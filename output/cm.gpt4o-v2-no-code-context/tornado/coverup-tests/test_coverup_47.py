# file: tornado/locks.py:398-413
# asked: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}
# gained: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from tornado.locks import _ReleasingContextManager

@pytest.fixture
def semaphore():
    return Semaphore(1)

@pytest.mark.gen_test
def test_semaphore_release_no_waiters(semaphore):
    # Test release when there are no waiters
    initial_value = semaphore._value
    semaphore.release()
    assert semaphore._value == initial_value + 1

@pytest.mark.gen_test
def test_semaphore_release_with_waiters(semaphore):
    # Test release when there are waiters
    semaphore._value = 0
    waiter = Future()
    semaphore._waiters.append(waiter)
    
    semaphore.release()
    
    assert semaphore._value == 0
    assert waiter.done()
    assert isinstance(waiter.result(), _ReleasingContextManager)

@pytest.mark.gen_test
def test_semaphore_release_with_done_waiter(semaphore):
    # Test release when the waiter is already done
    semaphore._value = 0
    waiter = Future()
    waiter.set_result(None)
    semaphore._waiters.append(waiter)
    
    semaphore.release()
    
    assert semaphore._value == 1
    assert waiter.done()
    assert waiter.result() is None
