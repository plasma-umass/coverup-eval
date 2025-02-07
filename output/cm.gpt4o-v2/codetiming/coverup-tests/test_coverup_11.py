# file: codetiming/_timers.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from codetiming._timers import Timers

def test_median_with_values():
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)
    assert timers.median("test") == 2.0

def test_median_no_values():
    timers = Timers()
    timers._timings["test"] = []
    assert timers.median("test") == 0.0

def test_median_single_value():
    timers = Timers()
    timers.add("test", 1.0)
    assert timers.median("test") == 1.0

@pytest.fixture(autouse=True)
def cleanup_timers():
    yield
    Timers().clear()
