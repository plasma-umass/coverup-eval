# file: tornado/locks.py:206-210
# asked: {"lines": [207, 208, 209], "branches": []}
# gained: {"lines": [207, 208, 209], "branches": []}

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
