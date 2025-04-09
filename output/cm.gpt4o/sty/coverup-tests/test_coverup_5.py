# file sty/primitive.py:72-76
# lines [72, 73, 74, 75, 76]
# branches []

import pytest
from sty.primitive import Register

def test_register_initialization():
    reg = Register()
    
    # Check initial values
    assert reg.renderfuncs == {}
    assert reg.is_muted is False
    assert reg.eightbit_call(42) == 42
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
