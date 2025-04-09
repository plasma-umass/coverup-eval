# file: codetiming/_timers.py:42-46
# asked: {"lines": [42, 44, 45, 46], "branches": [[44, 45], [44, 46]]}
# gained: {"lines": [42, 44, 45, 46], "branches": [[44, 45], [44, 46]]}

import pytest
from codetiming._timers import Timers

def test_apply_function_to_named_timer():
    timers = Timers()
    timers._timings = {'test_timer': [1.0, 2.0, 3.0]}
    
    def average(times):
        return sum(times) / len(times)
    
    result = timers.apply(average, 'test_timer')
    assert result == 2.0

def test_apply_function_to_nonexistent_timer():
    timers = Timers()
    timers._timings = {'test_timer': [1.0, 2.0, 3.0]}
    
    def average(times):
        return sum(times) / len(times)
    
    with pytest.raises(KeyError):
        timers.apply(average, 'nonexistent_timer')
