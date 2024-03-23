# file codetiming/_timer.py:67-70
# lines [67, 69, 70]
# branches []

import pytest
from codetiming import Timer

def test_timer_context_manager():
    with Timer() as t:
        assert hasattr(t, "_start_time"), "Timer should have '_start_time' attribute after entering context"
        assert t._start_time is not None, "_start_time should not be None after timer starts"
    # No need to check for _end_time as it is not an attribute of Timer class
