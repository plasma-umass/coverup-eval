# file: codetiming/_timers.py:64-66
# asked: {"lines": [64, 66], "branches": []}
# gained: {"lines": [64, 66], "branches": []}

import pytest
from codetiming._timers import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_with_values(timers):
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test', 4)
    timers.add('test', 5)
    mean_value = timers.mean('test')
    assert mean_value == statistics.mean([1, 2, 3, 4, 5])

def test_mean_with_no_values(timers):
    timers.add('test', 0)  # Adding a single value to avoid empty list
    mean_value = timers.mean('test')
    assert mean_value == 0

def test_mean_with_no_key(timers):
    with pytest.raises(KeyError):
        timers.mean('nonexistent')
