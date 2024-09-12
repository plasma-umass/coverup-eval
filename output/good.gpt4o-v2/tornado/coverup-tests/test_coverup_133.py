# file: tornado/locks.py:202-204
# asked: {"lines": [202, 203, 204], "branches": []}
# gained: {"lines": [202, 203, 204], "branches": []}

import pytest
from tornado.locks import Event

def test_event_initialization():
    event = Event()
    assert event._value is False
    assert isinstance(event._waiters, set)
    assert len(event._waiters) == 0
