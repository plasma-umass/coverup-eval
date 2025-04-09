# file: codetiming/_timers.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_timers_clear(timers):
    # Add some dummy data to timers
    timers.data['timer1'] = 1.0
    timers._timings['timer1'].append(1.0)
    
    # Ensure data is added
    assert 'timer1' in timers.data
    assert 'timer1' in timers._timings
    
    # Clear the timers
    timers.clear()
    
    # Ensure data is cleared
    assert not timers.data
    assert not timers._timings
