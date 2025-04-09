# file: codetiming/_timers.py:64-66
# asked: {"lines": [66], "branches": []}
# gained: {"lines": [66], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_mean_with_existing_timer(timers):
    timers._timings = {'test': [1.0, 2.0, 3.0]}
    result = timers.mean('test')
    assert result == 2.0

def test_mean_with_non_existing_timer(timers):
    timers._timings = {}
    with pytest.raises(KeyError):
        timers.mean('nonexistent')

def test_mean_with_empty_timer(timers):
    timers._timings = {'empty': []}
    result = timers.mean('empty')
    assert result == 0.0
