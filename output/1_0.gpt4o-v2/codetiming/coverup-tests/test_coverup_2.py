# file: codetiming/_timer.py:72-74
# asked: {"lines": [72, 74], "branches": []}
# gained: {"lines": [72, 74], "branches": []}

import pytest
from codetiming import Timer, TimerError

def test_timer_context_manager():
    timer = Timer()
    
    with timer:
        pass  # Just enter and exit the context to trigger __enter__ and __exit__
    
    assert timer._start_time is None  # Ensure the timer was stopped

def test_timer_context_manager_with_exception():
    timer = Timer()
    
    with pytest.raises(ValueError):
        with timer:
            raise ValueError("An error occurred")
    
    assert timer._start_time is None  # Ensure the timer was stopped even after an exception
