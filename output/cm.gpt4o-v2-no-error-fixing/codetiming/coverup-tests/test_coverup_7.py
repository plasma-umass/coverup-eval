# file: codetiming/_timers.py:60-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_max_with_existing_timer(timers):
    timers._timings = {'test_timer': [1.0, 2.0, 3.0]}
    assert timers.max('test_timer') == 3.0

def test_max_with_non_existing_timer(timers):
    with pytest.raises(KeyError):
        timers.max('non_existing_timer')

def test_max_with_empty_timer(timers):
    timers._timings = {'empty_timer': []}
    assert timers.max('empty_timer') == 0.0
