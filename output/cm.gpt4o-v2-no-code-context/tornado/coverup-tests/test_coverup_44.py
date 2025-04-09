# file: tornado/locks.py:216-226
# asked: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 224], [225, 226]]}
# gained: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 226]]}

import pytest
from tornado.locks import Event
from tornado.concurrent import Future

@pytest.fixture
def event():
    return Event()

def test_event_set(event):
    # Ensure the event is initially not set
    assert not event.is_set()

    # Create a future and add it to the waiters
    fut = Future()
    event._waiters.add(fut)

    # Set the event
    event.set()

    # Ensure the event is set
    assert event.is_set()

    # Ensure the future is completed
    assert fut.done()
    assert fut.result() is None

    # Clean up
    event._waiters.clear()
    event._value = False

def test_event_set_already_set(event):
    # Set the event initially
    event.set()

    # Ensure the event is set
    assert event.is_set()

    # Create a future and add it to the waiters
    fut = Future()
    event._waiters.add(fut)

    # Set the event again
    event.set()

    # Ensure the future is not added to waiters again
    assert not fut.done()

    # Clean up
    event._waiters.clear()
    event._value = False
