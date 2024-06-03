# file codetiming/_timers.py:42-46
# lines [42, 44, 45, 46]
# branches ['44->45', '44->46']

import pytest
from codetiming._timers import Timers

def test_timers_apply():
    timers = Timers()
    timers._timings = {'test_timer': [1.0, 2.0, 3.0]}
    
    # Test applying a function to an existing timer
    result = timers.apply(sum, 'test_timer')
    assert result == 6.0, "The sum of the timings should be 6.0"
    
    # Test applying a function to a non-existing timer
    with pytest.raises(KeyError) as excinfo:
        timers.apply(sum, 'non_existent_timer')
    assert str(excinfo.value) == "'non_existent_timer'", "Should raise KeyError for non-existent timer"
