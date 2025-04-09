# file: codetiming/_timers.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from codetiming._timers import Timers
import statistics

def test_median_existing_timer():
    timers = Timers()
    timers._timings['test'] = [1.0, 2.0, 3.0]
    assert timers.median('test') == 2.0

def test_median_empty_timer():
    timers = Timers()
    timers._timings['empty'] = []
    assert timers.median('empty') == 0.0

def test_median_single_value():
    timers = Timers()
    timers._timings['single'] = [42.0]
    assert timers.median('single') == 42.0

def test_median_raises_key_error():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median('nonexistent')
