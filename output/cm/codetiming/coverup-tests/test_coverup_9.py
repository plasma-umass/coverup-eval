# file codetiming/_timers.py:60-62
# lines [62]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_max_with_empty_values():
    # Create an instance of Timers
    timers = Timers()

    # Manually set the data to have an empty list for a specific key
    timers._timings['empty_timer'] = []

    # Call the max method with the key that has an empty list
    max_value = timers.max('empty_timer')

    # Assert that the max method returns 0 for an empty list
    assert max_value == 0, "Max value for an empty timer should be 0"
