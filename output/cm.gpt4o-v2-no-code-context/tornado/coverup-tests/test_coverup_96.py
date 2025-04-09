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
    repr_str = repr(event)
    assert repr_str == "<Event set>"

def test_event_repr_clear(event):
    repr_str = repr(event)
    assert repr_str == "<Event clear>"
