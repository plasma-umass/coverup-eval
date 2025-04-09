# file codetiming/_timers.py:24-28
# lines [24, 26, 27, 28]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_add():
    timers = Timers()
    timer_name = "test_timer"
    value = 2.5

    # Ensure the timer is not present initially
    assert timer_name not in timers

    # Add a timing value
    timers.add(timer_name, value)

    # Check if the timer was added with the correct value
    assert timers[timer_name] == value

    # Add another timing value
    additional_value = 1.5
    timers.add(timer_name, additional_value)

    # Check if the timer was updated with the new value
    assert timers[timer_name] == value + additional_value
