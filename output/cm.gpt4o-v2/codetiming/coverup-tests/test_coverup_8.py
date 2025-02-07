# file: codetiming/_timers.py:19-22
# asked: {"lines": [19, 21, 22], "branches": []}
# gained: {"lines": [19, 21, 22], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_init():
    timers = Timers()
    assert isinstance(timers, Timers)
    assert isinstance(timers._timings, dict)
    assert len(timers._timings) == 0

def test_timers_init_with_args(monkeypatch):
    def mock_setitem(self, name, value):
        self.data[name] = value

    monkeypatch.setattr(Timers, "__setitem__", mock_setitem)
    timers = Timers(a=1, b=2)
    assert timers['a'] == 1
    assert timers['b'] == 2
    assert isinstance(timers._timings, dict)
    assert len(timers._timings) == 0
