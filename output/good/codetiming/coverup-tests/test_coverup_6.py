# file codetiming/_timers.py:72-77
# lines [72, 74, 75, 76, 77]
# branches ['74->75', '74->77']

import pytest
from codetiming._timers import Timers
import math

def test_timers_stdev_with_single_timing(mocker):
    # Setup
    mocker.patch('codetiming._timers.statistics.stdev', return_value=1.0)
    timers = Timers()
    timers._timings = {"test_timer": [1.23]}

    # Exercise & Verify
    assert math.isnan(timers.stdev("test_timer")), "Standard deviation with a single timing should be NaN"

def test_timers_stdev_with_multiple_timings(mocker):
    # Setup
    expected_stdev = 0.5
    mocker.patch('codetiming._timers.statistics.stdev', return_value=expected_stdev)
    timers = Timers()
    timers._timings = {"test_timer": [1.23, 1.73]}

    # Exercise & Verify
    assert timers.stdev("test_timer") == expected_stdev, "Standard deviation with multiple timings should be calculated"

def test_timers_stdev_with_no_timings():
    # Setup
    timers = Timers()
    timers._timings = {}

    # Exercise & Verify
    with pytest.raises(KeyError):
        timers.stdev("test_timer")

# No top-level code is included as per the instructions.
