# file: tornado/locks.py:216-226
# asked: {"lines": [], "branches": [[225, 224]]}
# gained: {"lines": [], "branches": [[225, 224]]}

import pytest
from tornado.concurrent import Future
from tornado.locks import Event

@pytest.fixture
def event():
    e = Event()
    e._waiters = []
    e._value = False
    return e

def test_event_set_with_waiters(event):
    # Create a Future and add it to the event's waiters
    fut1 = Future()
    fut2 = Future()
    fut2.set_result(None)  # Make one future already done
    event._waiters.append(fut1)
    event._waiters.append(fut2)
    
    # Ensure the futures are in the correct state before setting the event
    assert not fut1.done()
    assert fut2.done()
    
    # Set the event
    event.set()
    
    # Ensure the first future is done after setting the event
    assert fut1.done()
    assert fut1.result() is None

def test_event_set_without_waiters(event):
    # Ensure there are no waiters initially
    assert len(event._waiters) == 0
    
    # Set the event
    event.set()
    
    # Ensure the event's value is set to True
    assert event._value is True

@pytest.fixture(autouse=True)
def cleanup_event(event):
    # Cleanup to avoid state pollution
    yield
    event._waiters.clear()
    event._value = False
