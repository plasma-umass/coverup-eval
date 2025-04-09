# file: codetiming/_timers.py:19-22
# asked: {"lines": [19, 21, 22], "branches": []}
# gained: {"lines": [19, 21, 22], "branches": []}

import pytest
from codetiming._timers import Timers
import math
import statistics

def test_timers_init():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert timers._timings == {}

def test_timers_add():
    timers = Timers()
    timers.add("test", 1.0)
    assert timers._timings["test"] == [1.0]
    assert timers["test"] == 1.0

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

def test_timers_apply():
    timers = Timers()
    timers.add("test", 1.0)
    result = timers.apply(sum, "test")
    assert result == 1.0
    with pytest.raises(KeyError):
        timers.apply(sum, "nonexistent")

def test_timers_count():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.count("test") == 2

def test_timers_total():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.total("test") == 3.0

def test_timers_min():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.min("test") == 1.0
    with pytest.raises(KeyError):
        timers.min("empty")

def test_timers_max():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.max("test") == 2.0
    with pytest.raises(KeyError):
        timers.max("empty")

def test_timers_mean():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.mean("test") == 1.5
    with pytest.raises(KeyError):
        timers.mean("empty")

def test_timers_median():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 3.0)
    assert timers.median("test") == 2.0
    with pytest.raises(KeyError):
        timers.median("empty")

def test_timers_stdev():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 3.0)
    assert math.isnan(timers.stdev("test")) == False
    with pytest.raises(KeyError):
        timers.stdev("empty")
