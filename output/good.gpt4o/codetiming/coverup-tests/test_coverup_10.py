# file codetiming/_timers.py:60-62
# lines [62]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_max():
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)
    
    # Test max with existing timer
    assert timers.max('test_timer') == 3.0
    
    # Test max with non-existing timer
    with pytest.raises(KeyError):
        timers.max('non_existing_timer')
