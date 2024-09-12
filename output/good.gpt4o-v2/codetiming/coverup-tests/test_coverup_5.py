# file: codetiming/_timers.py:72-77
# asked: {"lines": [72, 74, 75, 76, 77], "branches": [[74, 75], [74, 77]]}
# gained: {"lines": [72, 74, 75, 76, 77], "branches": [[74, 75], [74, 77]]}

import pytest
from codetiming._timers import Timers
import math
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_stdev_with_values(timers):
    timers._timings['test'] = [1.0, 2.0, 3.0]
    result = timers.stdev('test')
    expected = statistics.stdev([1.0, 2.0, 3.0])
    assert result == expected, f"Expected {expected}, but got {result}"

def test_stdev_with_single_value(timers):
    timers._timings['test'] = [1.0]
    result = timers.stdev('test')
    assert math.isnan(result), f"Expected NaN, but got {result}"

def test_stdev_key_error(timers):
    with pytest.raises(KeyError) as excinfo:
        timers.stdev('nonexistent')
    assert str(excinfo.value) == "'nonexistent'", f"Expected KeyError with 'nonexistent', but got {excinfo.value}"
