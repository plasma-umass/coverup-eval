# file tornado/locks.py:202-204
# lines [202, 203, 204]
# branches []

import pytest
from tornado.locks import Event
from tornado.concurrent import Future

@pytest.fixture
def event():
    return Event()

def test_event_initial_state(event):
    assert not event._value
    assert isinstance(event._waiters, set)
    assert len(event._waiters) == 0

def test_event_set(event):
    event._value = True
    assert event._value

def test_event_waiters(event):
    future = Future()
    event._waiters.add(future)
    assert len(event._waiters) == 1
    assert future in event._waiters

def test_event_cleanup(event):
    future = Future()
    event._waiters.add(future)
    event._waiters.remove(future)
    assert len(event._waiters) == 0
    assert future not in event._waiters
