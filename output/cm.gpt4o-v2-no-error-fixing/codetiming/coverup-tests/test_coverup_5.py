# file: codetiming/_timers.py:48-50
# asked: {"lines": [50], "branches": []}
# gained: {"lines": [50], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_count():
    timers = Timers()
    timers._timings = {'test_timer': [1.0, 2.0, 3.0]}
    
    # Test the count method
    assert timers.count('test_timer') == 3

    # Test the KeyError exception
    with pytest.raises(KeyError):
        timers.count('non_existent_timer')
