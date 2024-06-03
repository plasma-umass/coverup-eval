# file codetiming/_timers.py:35-40
# lines [37, 38]
# branches []

import pytest
from codetiming._timers import Timers

def test_timers_setitem_raises_typeerror():
    timers = Timers()
    with pytest.raises(TypeError) as excinfo:
        timers['test_timer'] = 123.456
    assert str(excinfo.value) == (
        "'Timers' does not support item assignment. Use '.add()' to update values."
    )
