# file codetiming/_timers.py:30-33
# lines [30, 32, 33]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_clear():
    timers = Timers()
    timers.data['test_timer'] = 1.23
    timers._timings = {'test_timer': [1.23, 2.34]}

    assert 'test_timer' in timers.data
    assert 'test_timer' in timers._timings

    timers.clear()

    assert 'test_timer' not in timers.data
    assert 'test_timer' not in timers._timings
