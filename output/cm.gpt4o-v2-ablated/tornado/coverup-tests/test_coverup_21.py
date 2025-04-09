# file: tornado/locks.py:398-413
# asked: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}
# gained: {"lines": [398, 400, 401, 402, 403, 404, 412, 413], "branches": [[401, 0], [401, 402], [403, 401], [403, 404]]}

import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
from collections import deque

@pytest.fixture
def semaphore():
    sem = Semaphore()
    sem._value = 0
    sem._waiters = deque()
    return sem

def test_semaphore_release_no_waiters(semaphore):
    semaphore.release()
    assert semaphore._value == 1

def test_semaphore_release_with_waiters(semaphore):
    future1 = Future()
    future2 = Future()
    semaphore._waiters.append(future1)
    semaphore._waiters.append(future2)
    
    semaphore.release()
    
    assert semaphore._value == 0
    assert future1.done()
    assert not future2.done()

def test_semaphore_release_waiter_already_done(semaphore):
    future1 = Future()
    future1.set_result(None)
    future2 = Future()
    semaphore._waiters.append(future1)
    semaphore._waiters.append(future2)
    
    semaphore.release()
    
    assert semaphore._value == 0
    assert future2.done()
    assert future1.done()
