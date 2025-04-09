# file: codetiming/_timers.py:56-58
# asked: {"lines": [56, 58], "branches": []}
# gained: {"lines": [56, 58], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_min():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)
    
    assert timers.min("test") == 1.0

    with pytest.raises(KeyError):
        timers.min("nonexistent")

def test_timers_add():
    timers = Timers()
    timers.add("test", 1.0)
    assert timers._timings["test"] == [1.0]
    assert timers.data["test"] == 1.0

    timers.add("test", 2.0)
    assert timers._timings["test"] == [1.0, 2.0]
    assert timers.data["test"] == 3.0

def test_timers_clear():
    timers = Timers()
    timers.add("test", 1.0)
    timers.clear()
    assert timers._timings == {}
    assert timers.data == {}

def test_timers_setitem():
    timers = Timers()
    with pytest.raises(TypeError):
        timers["test"] = 1.0
