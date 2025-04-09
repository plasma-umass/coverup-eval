# file: tornado/locks.py:145-155
# asked: {"lines": [149, 150, 151, 152, 155], "branches": [[148, 149], [150, 148], [150, 151], [154, 155]]}
# gained: {"lines": [149, 150, 151, 152, 155], "branches": [[148, 149], [150, 148], [150, 151], [154, 155]]}

import pytest
from unittest.mock import Mock
from tornado.locks import Condition
from tornado.concurrent import Future

@pytest.fixture
def condition():
    return Condition()

def test_notify_no_waiters(condition):
    # Test notify with no waiters
    condition.notify()

def test_notify_with_waiters(condition):
    # Test notify with waiters
    future1 = Future()
    future2 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(2)
    
    assert future1.done()
    assert future2.done()
    assert future1.result() is True
    assert future2.result() is True

def test_notify_with_some_done_waiters(condition):
    # Test notify with some waiters already done
    future1 = Future()
    future2 = Future()
    future1.set_result(None)  # Simulate future1 already done
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    
    condition.notify(2)
    
    assert future2.done()
    assert future2.result() is True

def test_notify_more_than_waiters(condition):
    # Test notify with n greater than the number of waiters
    future1 = Future()
    condition._waiters.append(future1)
    
    condition.notify(2)
    
    assert future1.done()
    assert future1.result() is True
