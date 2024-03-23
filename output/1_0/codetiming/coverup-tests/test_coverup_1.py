# file codetiming/_timer.py:18-19
# lines [18, 19]
# branches []

import pytest
from codetiming import Timer
from codetiming._timer import TimerError

def test_timer_error():
    with pytest.raises(TimerError):
        raise TimerError("This is a TimerError test.")
