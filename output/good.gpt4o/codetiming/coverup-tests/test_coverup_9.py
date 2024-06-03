# file codetiming/_timers.py:72-77
# lines [74, 75, 76, 77]
# branches ['74->75', '74->77']

import pytest
from codetiming._timers import Timers
import math
import statistics

def test_timers_stdev_key_error():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev("non_existent_timer")

def test_timers_stdev_nan():
    timers = Timers()
    timers._timings = {"test_timer": [1.0]}
    result = timers.stdev("test_timer")
    assert math.isnan(result), "Expected NaN for single timing entry"

def test_timers_stdev_value():
    timers = Timers()
    timers._timings = {"test_timer": [1.0, 2.0, 3.0]}
    result = timers.stdev("test_timer")
    expected = statistics.stdev([1.0, 2.0, 3.0])
    assert result == expected, f"Expected {expected}, got {result}"
