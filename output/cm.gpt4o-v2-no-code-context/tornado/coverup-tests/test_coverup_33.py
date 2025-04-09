# file: tornado/locks.py:145-155
# asked: {"lines": [145, 147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}
# gained: {"lines": [145, 147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}

import pytest
from tornado.locks import Condition
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

@pytest.fixture
def condition():
    return Condition()

def test_notify_no_waiters(condition):
    # Test notify when there are no waiters
    condition.notify()
    assert len(condition._waiters) == 0

def test_notify_with_waiters(condition):
    # Test notify when there are waiters
    future1 = Future()
    future2 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(1)
    
    assert future1.done()
    assert not future2.done()

def test_notify_with_timed_out_waiters(condition):
    # Test notify when there are waiters that have timed out
    future1 = Future()
    future2 = Future()
    future1.set_result(None)  # Simulate timeout
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(1)
    
    assert future1.done()  # future1 was already done
    assert future2.done()  # future2 should be notified

def test_notify_all_waiters(condition):
    # Test notify all waiters
    future1 = Future()
    future2 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(2)
    
    assert future1.done()
    assert future2.done()

def test_notify_more_than_waiters(condition):
    # Test notify more than the number of waiters
    future1 = Future()
    future2 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(3)
    
    assert future1.done()
    assert future2.done()
