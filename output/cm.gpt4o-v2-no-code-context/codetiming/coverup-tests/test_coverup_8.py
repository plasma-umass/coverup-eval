# file: codetiming/_timers.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from codetiming._timers import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_median_with_values(timers):
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test', 4)
    timers.add('test', 5)
    assert timers.median('test') == 3

def test_median_with_no_values(timers):
    timers._timings['test'] = []
    assert timers.median('test') == 0

def test_median_with_single_value(timers):
    timers.add('test', 42)
    assert timers.median('test') == 42

def test_median_with_even_number_of_values(timers):
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test', 4)
    assert timers.median('test') == 2.5
