# file codetiming/_timers.py:16-18
# lines [16, 17]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert isinstance(timers.data, dict)
    assert len(timers) == 0

def test_timers_add_and_retrieve():
    timers = Timers()
    timers.add('test_timer', 123)
    assert 'test_timer' in timers
    assert timers['test_timer'] == 123

def test_timers_delete():
    timers = Timers()
    timers.add('test_timer', 123)
    del timers['test_timer']
    assert 'test_timer' not in timers

def test_timers_clear():
    timers = Timers()
    timers.add('test_timer1', 123)
    timers.add('test_timer2', 456)
    timers.clear()
    assert len(timers) == 0
