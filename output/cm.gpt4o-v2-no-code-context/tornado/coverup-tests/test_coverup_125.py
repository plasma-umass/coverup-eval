# file: tornado/locks.py:202-204
# asked: {"lines": [202, 203, 204], "branches": []}
# gained: {"lines": [202, 203, 204], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_initial_state(event):
    assert not event._value
    assert isinstance(event._waiters, set)
    assert len(event._waiters) == 0
