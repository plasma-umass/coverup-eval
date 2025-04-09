# file: tornado/locks.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}
# gained: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_condition_repr_no_waiters(condition):
    assert repr(condition) == "<Condition>"

def test_condition_repr_with_waiters(condition, monkeypatch):
    # Mock the _waiters attribute to simulate waiters
    monkeypatch.setattr(condition, '_waiters', [1, 2, 3])
    assert repr(condition) == "<Condition waiters[3]>"

