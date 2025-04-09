# file: codetiming/_timers.py:48-50
# asked: {"lines": [48, 50], "branches": []}
# gained: {"lines": [48, 50], "branches": []}

import pytest
import math
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_add(timers):
    timers.add("test", 1.0)
    assert timers._timings["test"] == [1.0]
    assert timers.data["test"] == 1.0

def test_clear(timers):
    timers.add("test", 1.0)
    timers.clear()
    assert timers._timings == {}
    assert timers.data == {}

def test_setitem(timers):
    with pytest.raises(TypeError):
        timers["test"] = 1.0

def test_apply(timers):
    timers.add("test", 1.0)
    result = timers.apply(sum, "test")
    assert result == 1.0

    with pytest.raises(KeyError):
        timers.apply(sum, "nonexistent")

def test_count(timers):
    timers.add("test", 1.0)
    assert timers.count("test") == 1

def test_total(timers):
    timers.add("test", 1.0)
    assert timers.total("test") == 1.0

def test_min(timers):
    timers.add("test", 1.0)
    assert timers.min("test") == 1.0

def test_max(timers):
    timers.add("test", 1.0)
    assert timers.max("test") == 1.0

def test_mean(timers):
    timers.add("test", 1.0)
    assert timers.mean("test") == 1.0

def test_median(timers):
    timers.add("test", 1.0)
    assert timers.median("test") == 1.0

def test_stdev(timers):
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    assert timers.stdev("test") == pytest.approx(0.7071, rel=1e-2)

    timers.clear()
    timers.add("test", 1.0)
    assert math.isnan(timers.stdev("test"))
