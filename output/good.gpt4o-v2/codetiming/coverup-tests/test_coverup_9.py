# file: codetiming/_timers.py:35-40
# asked: {"lines": [35, 37, 38], "branches": []}
# gained: {"lines": [35, 37, 38], "branches": []}

import pytest
from codetiming._timers import Timers
import re

def test_timers_setitem_raises_typeerror():
    timers = Timers()
    with pytest.raises(TypeError, match=re.escape("'Timers' does not support item assignment. Use '.add()' to update values.")):
        timers["test"] = 1.0
