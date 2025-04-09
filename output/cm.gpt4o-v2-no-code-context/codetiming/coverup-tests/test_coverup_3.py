# file: codetiming/_timers.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_clear():
    timers = Timers()
    timers.data['test'] = 1
    timers._timings = {'test': 1}
    
    assert 'test' in timers.data
    assert 'test' in timers._timings
    
    timers.clear()
    
    assert 'test' not in timers.data
    assert 'test' not in timers._timings
