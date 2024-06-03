# file codetiming/_timers.py:52-54
# lines [52, 54]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_total():
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)
    
    total_time = timers.total('test_timer')
    
    assert total_time == 6.0

    # Clean up
    timers.clear()
