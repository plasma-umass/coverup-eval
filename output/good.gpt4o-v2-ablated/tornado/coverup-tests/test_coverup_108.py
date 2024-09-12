# file: tornado/locks.py:228-233
# asked: {"lines": [228, 233], "branches": []}
# gained: {"lines": [228, 233], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_initial_state(event):
    assert not event._value

def test_event_clear(event):
    event._value = True
    event.clear()
    assert not event._value
