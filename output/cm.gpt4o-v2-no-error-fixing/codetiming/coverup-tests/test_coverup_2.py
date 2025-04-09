# file: codetiming/_timers.py:24-28
# asked: {"lines": [24, 26, 27, 28], "branches": []}
# gained: {"lines": [24, 26, 27, 28], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_add_new_timer(timers):
    timers.add("test_timer", 1.0)
    assert timers._timings["test_timer"] == [1.0]
    assert timers.data["test_timer"] == 1.0

def test_add_existing_timer(timers):
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    assert timers._timings["test_timer"] == [1.0, 2.0]
    assert timers.data["test_timer"] == 3.0
