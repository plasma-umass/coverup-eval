# file: codetiming/_timers.py:56-58
# asked: {"lines": [56, 58], "branches": []}
# gained: {"lines": [56, 58], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_min_with_values(timers):
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)
    assert timers.min("test") == 1.0

def test_min_no_values(timers):
    timers._timings["test"] = []
    assert timers.min("test") == 0.0

def test_min_with_zero(timers):
    timers.add("test", 0.0)
    assert timers.min("test") == 0.0
