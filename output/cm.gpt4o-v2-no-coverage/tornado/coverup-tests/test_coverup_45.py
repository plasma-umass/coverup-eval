# file: tornado/locks.py:216-226
# asked: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 224], [225, 226]]}
# gained: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 226]]}

import pytest
from tornado.concurrent import Future
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_set(event):
    # Initially, the internal flag should be False
    assert not event._value

    # Create a future and add it to the waiters
    fut = Future()
    event._waiters.add(fut)

    # Call set and check the internal flag and future result
    event.set()
    assert event._value
    assert fut.done()
    assert fut.result() is None

    # Clean up
    event._waiters.clear()
    event._value = False

def test_event_set_already_set(event):
    # Set the internal flag to True
    event._value = True

    # Create a future and add it to the waiters
    fut = Future()
    event._waiters.add(fut)

    # Call set and check that the future is not changed
    event.set()
    assert event._value
    assert not fut.done()

    # Clean up
    event._waiters.clear()
    event._value = False
