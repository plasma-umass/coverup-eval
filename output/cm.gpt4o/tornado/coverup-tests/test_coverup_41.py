# file tornado/locks.py:216-226
# lines [216, 221, 222, 224, 225, 226]
# branches ['221->exit', '221->222', '224->exit', '224->225', '225->224', '225->226']

import pytest
from tornado.locks import Event
from tornado.concurrent import Future

@pytest.fixture
def event():
    return Event()

def test_event_set(event, mocker):
    # Mock the _waiters list with Futures
    future1 = Future()
    future2 = Future()
    event._waiters = [future1, future2]
    event._value = False

    # Set the event
    event.set()

    # Assert that the internal flag is set to True
    assert event._value is True

    # Assert that all futures in _waiters are set
    assert future1.done() is True
    assert future2.done() is True
    assert future1.result() is None
    assert future2.result() is None

    # Clean up
    event._waiters = []
    event._value = False
