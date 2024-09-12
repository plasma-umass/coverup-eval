# file: codetiming/_timers.py:48-50
# asked: {"lines": [48, 50], "branches": []}
# gained: {"lines": [48, 50], "branches": []}

import pytest
from codetiming._timers import Timers

def test_timers_count():
    timers = Timers()
    timers._timings['test'] = [1.0, 2.0, 3.0]
    
    assert timers.count('test') == 3

    with pytest.raises(KeyError):
        timers.count('nonexistent')
