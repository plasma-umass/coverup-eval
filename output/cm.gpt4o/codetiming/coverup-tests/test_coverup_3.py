# file codetiming/_timers.py:48-50
# lines [48, 50]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_count():
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)
    
    count = timers.count('test_timer')
    
    assert count == 3

    # Clean up
    timers.clear()
