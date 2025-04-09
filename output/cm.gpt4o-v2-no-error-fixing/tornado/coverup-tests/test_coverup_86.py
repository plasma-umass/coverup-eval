# file: tornado/locks.py:206-210
# asked: {"lines": [206, 207, 208, 209], "branches": []}
# gained: {"lines": [206, 207, 208, 209], "branches": []}

import pytest
from tornado.locks import Event

def test_event_repr_when_set():
    event = Event()
    event.set()
    assert repr(event) == "<Event set>"

def test_event_repr_when_clear():
    event = Event()
    event.clear()
    assert repr(event) == "<Event clear>"
