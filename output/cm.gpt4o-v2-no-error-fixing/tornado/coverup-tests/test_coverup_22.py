# file: tornado/locks.py:145-155
# asked: {"lines": [145, 147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}
# gained: {"lines": [145, 147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 154], [150, 148], [150, 151], [154, 0], [154, 155]]}

import pytest
from tornado.locks import Condition
from tornado.concurrent import Future

@pytest.fixture
def condition():
    return Condition()

def test_notify_no_waiters(condition):
    # Test when there are no waiters
    condition.notify()
    assert len(condition._waiters) == 0

def test_notify_with_waiters(condition):
    # Test when there are waiters
    future1 = Future()
    future2 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)

    condition.notify(1)
    assert future1.done()
    assert not future2.done()

    condition.notify(1)
    assert future2.done()

def test_notify_with_timed_out_waiter(condition):
    # Test when a waiter has timed out
    future1 = Future()
    future2 = Future()
    future1.set_result(None)  # Simulate timeout by setting result
    condition._waiters.append(future1)
    condition._waiters.append(future2)

    condition.notify(1)
    assert future2.done()
    assert future1.done()  # future1 was already done

def test_notify_multiple_waiters(condition):
    # Test notifying multiple waiters
    future1 = Future()
    future2 = Future()
    future3 = Future()
    condition._waiters.append(future1)
    condition._waiters.append(future2)
    condition._waiters.append(future3)

    condition.notify(2)
    assert future1.done()
    assert future2.done()
    assert not future3.done()

    condition.notify(1)
    assert future3.done()
