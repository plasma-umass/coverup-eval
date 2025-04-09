# file: sty/primitive.py:72-76
# asked: {"lines": [72, 73, 74, 75, 76], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76], "branches": []}

import pytest
from sty.primitive import Register

def test_register_init():
    reg = Register()
    
    # Verify that renderfuncs is initialized as an empty dictionary
    assert reg.renderfuncs == {}
    
    # Verify that is_muted is initialized as False
    assert reg.is_muted is False
    
    # Verify that eightbit_call is a lambda function that returns its input
    assert reg.eightbit_call(123) == 123
    
    # Verify that rgb_call is a lambda function that returns a tuple of its inputs
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
