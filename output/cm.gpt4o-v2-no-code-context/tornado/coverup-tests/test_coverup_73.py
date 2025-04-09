# file: tornado/locks.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}
# gained: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}

import pytest
from tornado.locks import Condition

@pytest.fixture
def condition():
    return Condition()

def test_condition_repr_no_waiters(condition):
    repr_str = repr(condition)
    assert repr_str == "<Condition>"

def test_condition_repr_with_waiters(condition, monkeypatch):
    class FakeWaiter:
        pass

    fake_waiters = [FakeWaiter(), FakeWaiter()]
    monkeypatch.setattr(condition, '_waiters', fake_waiters)
    
    repr_str = repr(condition)
    assert repr_str == "<Condition waiters[2]>"

