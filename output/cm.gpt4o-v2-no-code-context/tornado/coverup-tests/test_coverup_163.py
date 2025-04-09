# file: tornado/locks.py:212-214
# asked: {"lines": [212, 214], "branches": []}
# gained: {"lines": [212, 214], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_is_set_initially_false(event):
    assert not event.is_set()

def test_event_is_set_after_set(event):
    event.set()
    assert event.is_set()

def test_event_is_set_after_clear(event):
    event.set()
    event.clear()
    assert not event.is_set()
