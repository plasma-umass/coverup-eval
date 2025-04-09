# file: tornado/locks.py:212-214
# asked: {"lines": [212, 214], "branches": []}
# gained: {"lines": [212, 214], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_initial_state(event):
    assert not event.is_set()

def test_event_set(event):
    event.set()
    assert event.is_set()

def test_event_clear(event):
    event.set()
    event.clear()
    assert not event.is_set()
