# file: codetiming/_timers.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_clear():
    timers = Timers()
    timers.data = {'timer1': 1, 'timer2': 2}
    timers._timings = {'timer1': [0.1, 0.2], 'timer2': [0.3, 0.4]}
    
    timers.clear()
    
    assert timers.data == {}
    assert timers._timings == {}
