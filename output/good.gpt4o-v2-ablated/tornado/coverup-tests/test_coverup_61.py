# file: tornado/locks.py:206-210
# asked: {"lines": [206, 207, 208, 209], "branches": []}
# gained: {"lines": [206, 207, 208, 209], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_repr_set(event):
    event.set()
    assert repr(event) == "<Event set>"

def test_event_repr_clear(event):
    event.clear()
    assert repr(event) == "<Event clear>"

def test_event_initial_state(event):
    assert repr(event) == "<Event clear>"

def test_event_set_state(event):
    event.set()
    assert event.is_set() is True
    assert repr(event) == "<Event set>"

def test_event_clear_state(event):
    event.set()
    event.clear()
    assert event.is_set() is False
    assert repr(event) == "<Event clear>"
