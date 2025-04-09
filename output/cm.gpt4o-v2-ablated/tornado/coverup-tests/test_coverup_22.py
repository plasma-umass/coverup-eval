# file: tornado/locks.py:216-226
# asked: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 224], [225, 226]]}
# gained: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 226]]}

import pytest
from tornado.concurrent import Future
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_set(event, mocker):
    # Mocking the _value and _waiters attributes
    mocker.patch.object(event, '_value', False)
    future1 = Future()
    future2 = Future()
    mocker.patch.object(event, '_waiters', [future1, future2])

    # Call the set method
    event.set()

    # Assertions to verify postconditions
    assert event._value is True
    assert future1.done()
    assert future2.done()
    assert future1.result() is None
    assert future2.result() is None

def test_event_set_already_set(event, mocker):
    # Mocking the _value attribute to be already True
    mocker.patch.object(event, '_value', True)
    future1 = Future()
    future2 = Future()
    mocker.patch.object(event, '_waiters', [future1, future2])

    # Call the set method
    event.set()

    # Assertions to verify postconditions
    assert event._value is True
    assert not future1.done()
    assert not future2.done()
