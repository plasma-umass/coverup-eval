# file codetiming/_timers.py:64-66
# lines [64, 66]
# branches []

import pytest
from unittest.mock import patch
from codetiming._timers import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_with_values(timers):
    timers.add('test_timer', 1)
    timers.add('test_timer', 2)
    timers.add('test_timer', 3)
    timers.add('test_timer', 4)
    timers.add('test_timer', 5)
    assert timers.mean('test_timer') == statistics.mean([1, 2, 3, 4, 5])

def test_mean_with_no_values(timers):
    timers.add('empty_timer', 0)
    assert timers.mean('empty_timer') == 0

def test_mean_with_nonexistent_timer(timers):
    with pytest.raises(KeyError):
        timers.mean('nonexistent_timer')
