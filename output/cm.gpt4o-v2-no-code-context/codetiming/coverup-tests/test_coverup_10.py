# file: codetiming/_timers.py:56-58
# asked: {"lines": [58], "branches": []}
# gained: {"lines": [58], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_min_with_existing_timer(timers):
    timers.add('test', 1.0)
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    assert timers.min('test') == 1.0

def test_min_with_empty_timer(timers):
    timers.add('test', 0.0)  # Adding a single zero value to simulate an empty timer
    assert timers.min('test') == 0.0

def test_min_with_nonexistent_timer(timers):
    with pytest.raises(KeyError):
        timers.min('nonexistent')
