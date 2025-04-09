# file: tornado/locks.py:206-210
# asked: {"lines": [206, 207, 208, 209], "branches": []}
# gained: {"lines": [206, 207, 208, 209], "branches": []}

import pytest
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_repr_set(monkeypatch, event):
    monkeypatch.setattr(event, '_value', True)
    assert repr(event) == "<Event set>"

def test_event_repr_clear(monkeypatch, event):
    monkeypatch.setattr(event, '_value', False)
    assert repr(event) == "<Event clear>"
