# file sty/primitive.py:72-76
# lines [72, 73, 74, 75, 76]
# branches []

import pytest
from sty.primitive import Register

def test_register_init():
    # Test the initialization of the Register class
    reg = Register()

    # Assertions to check the initial state of the Register object
    assert isinstance(reg.renderfuncs, dict)
    assert reg.is_muted == False
    assert reg.eightbit_call(100) == 100
    assert reg.rgb_call(10, 20, 30) == (10, 20, 30)
