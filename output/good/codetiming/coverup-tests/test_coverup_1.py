# file codetiming/_timers.py:35-40
# lines [35, 37, 38]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_setitem_disallowed():
    timers = Timers()
    with pytest.raises(TypeError) as exc_info:
        timers["timer1"] = 100.0
    assert str(exc_info.value) == "'Timers' does not support item assignment. Use '.add()' to update values."
