# file: codetiming/_timers.py:72-77
# asked: {"lines": [72, 74, 75, 76, 77], "branches": [[74, 75], [74, 77]]}
# gained: {"lines": [72, 74, 75, 76, 77], "branches": [[74, 75], [74, 77]]}

import pytest
from codetiming._timers import Timers
import statistics
import math

@pytest.fixture
def timers():
    return Timers()

def test_stdev_with_valid_name(timers):
    timers._timings = {'test': [1.0, 2.0, 3.0]}
    result = timers.stdev('test')
    assert result == statistics.stdev([1.0, 2.0, 3.0])

def test_stdev_with_single_value(timers):
    timers._timings = {'test': [1.0]}
    result = timers.stdev('test')
    assert math.isnan(result)

def test_stdev_with_invalid_name(timers):
    timers._timings = {'test': [1.0, 2.0, 3.0]}
    with pytest.raises(KeyError):
        timers.stdev('invalid')
