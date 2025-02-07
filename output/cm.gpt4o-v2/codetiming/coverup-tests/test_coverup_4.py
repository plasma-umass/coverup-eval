# file: codetiming/_timers.py:42-46
# asked: {"lines": [42, 44, 45, 46], "branches": [[44, 45], [44, 46]]}
# gained: {"lines": [42, 44, 45, 46], "branches": [[44, 45], [44, 46]]}

import pytest
from codetiming._timers import Timers

def test_apply_with_existing_timer(monkeypatch):
    timings = {'timer1': [1.0, 2.0, 3.0]}
    timers = Timers()
    monkeypatch.setattr(timers, '_timings', timings)
    
    result = timers.apply(sum, 'timer1')
    assert result == 6.0

def test_apply_with_non_existing_timer(monkeypatch):
    timings = {'timer1': [1.0, 2.0, 3.0]}
    timers = Timers()
    monkeypatch.setattr(timers, '_timings', timings)
    
    with pytest.raises(KeyError) as excinfo:
        timers.apply(sum, 'timer2')
    assert str(excinfo.value) == "'timer2'"
