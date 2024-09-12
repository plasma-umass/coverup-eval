# file: codetiming/_timers.py:60-62
# asked: {"lines": [60, 62], "branches": []}
# gained: {"lines": [60, 62], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_max_with_values(timers):
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)
    assert timers.max("test") == 3.0

def test_max_without_values(timers):
    timers._timings["test"] = []
    assert timers.max("test") == 0.0

def test_max_with_monkeypatch(monkeypatch, timers):
    def mock_apply(func, name):
        return func([1.0, 2.0, 3.0])
    
    monkeypatch.setattr(timers, 'apply', mock_apply)
    assert timers.max("test") == 3.0
