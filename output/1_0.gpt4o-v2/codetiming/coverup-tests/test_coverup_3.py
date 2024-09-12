# file: codetiming/_timer.py:33-38
# asked: {"lines": [33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}
# gained: {"lines": [33, 35, 36, 38], "branches": [[35, 36], [35, 38]]}

import pytest
from codetiming import Timer, TimerError
import re

def test_timer_start():
    timer = Timer()
    
    # Test starting the timer
    timer.start()
    assert timer._start_time is not None
    
    # Test starting the timer when it's already running
    with pytest.raises(TimerError, match=re.escape("Timer is running. Use .stop() to stop it")):
        timer.start()

    # Clean up
    timer._start_time = None
