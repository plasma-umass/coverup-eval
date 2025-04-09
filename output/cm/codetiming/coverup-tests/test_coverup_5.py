# file codetiming/_timers.py:52-54
# lines [52, 54]
# branches []

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_timers_total(timers):
    # Add some mock timers using the add method
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    timers.add("timer2", 0.5)
    timers.add("timer2", 0.5)

    # Test the total method for timer1
    total_time_timer1 = timers.total("timer1")
    assert total_time_timer1 == 6.0, "The total time for timer1 should be 6.0"

    # Test the total method for timer2
    total_time_timer2 = timers.total("timer2")
    assert total_time_timer2 == 1.0, "The total time for timer2 should be 1.0"

    # Test the total method for a non-existing timer
    with pytest.raises(KeyError):
        timers.total("timer3")
