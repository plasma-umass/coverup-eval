# file pytutils/timers.py:7-29
# lines [17]
# branches []

import pytest
from pytutils.timers import Timer
import time

def test_timer_repr(mocker):
    # Mock time to ensure no side effects on other tests
    mocker.patch('time.time', return_value=1234567890.123456)

    with Timer(name='TestTimer', verbose=True) as timer:
        time.sleep(0.001)  # Simulate some operation

    # Check if the __repr__ method is called and returns the expected string
    assert repr(timer) == 'Timer(TestTimer)', "The __repr__ method did not return the expected string."

    # Clean up by stopping the mock
    mocker.stopall()
