# file: tornado/locks.py:31-50
# asked: {"lines": [31, 32, 41, 42, 43, 45, 47, 48, 49, 50], "branches": [[48, 0], [48, 49]]}
# gained: {"lines": [31, 32, 41, 42, 43, 45, 47, 48, 49, 50], "branches": [[48, 0], [48, 49]]}

import collections
from tornado.concurrent import Future
import pytest
from tornado.locks import _TimeoutGarbageCollector

@pytest.fixture
def timeout_gc():
    return _TimeoutGarbageCollector()

def test_initial_state(timeout_gc):
    assert len(timeout_gc._waiters) == 0
    assert timeout_gc._timeouts == 0

def test_garbage_collect_no_waiters(timeout_gc):
    timeout_gc._garbage_collect()
    assert len(timeout_gc._waiters) == 0
    assert timeout_gc._timeouts == 1

def test_garbage_collect_with_waiters(timeout_gc):
    future1 = Future()
    future2 = Future()
    timeout_gc._waiters.append(future1)
    timeout_gc._waiters.append(future2)
    
    timeout_gc._garbage_collect()
    assert len(timeout_gc._waiters) == 2
    assert timeout_gc._timeouts == 1

def test_garbage_collect_with_done_waiters(timeout_gc):
    future1 = Future()
    future2 = Future()
    future1.set_result(None)
    timeout_gc._waiters.append(future1)
    timeout_gc._waiters.append(future2)
    
    for _ in range(101):
        timeout_gc._garbage_collect()
    
    assert len(timeout_gc._waiters) == 1
    assert timeout_gc._timeouts == 0
    assert timeout_gc._waiters[0] is future2
