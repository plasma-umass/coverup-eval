# file codetiming/_timers.py:19-22
# lines [19, 21, 22]
# branches []

import pytest
from codetiming._timers import Timers
from collections import UserDict

def test_timers_initialization():
    # Test the initialization of the Timers class and the private _timings attribute
    timers = Timers()
    assert isinstance(timers, UserDict), "Timers instance should be a UserDict"
    assert hasattr(timers, '_timings'), "Timers instance should have a _timings attribute"
    assert isinstance(timers._timings, dict), "The _timings attribute should be a dictionary"
    assert all(isinstance(v, list) for v in timers._timings.values()), "All values in _timings should be lists"

def test_timers_with_initial_data():
    # Test the Timers class with initial data
    timers = Timers()
    timers.add('timer1', 1.23)
    timers.add('timer2', 4.56)
    assert 'timer1' in timers, "Timers instance should contain 'timer1'"
    assert 'timer2' in timers, "Timers instance should contain 'timer2'"
    assert timers._timings['timer1'] == [1.23], "The _timings attribute should reflect the added data"
    assert timers._timings['timer2'] == [4.56], "The _timings attribute should reflect the added data"
