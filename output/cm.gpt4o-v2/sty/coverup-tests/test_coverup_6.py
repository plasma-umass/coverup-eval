# file: sty/primitive.py:72-76
# asked: {"lines": [72, 73, 74, 75, 76], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

def test_register_init():
    reg = Register()
    
    # Check that renderfuncs is initialized as an empty dictionary
    assert isinstance(reg.renderfuncs, dict)
    assert len(reg.renderfuncs) == 0
    
    # Check that is_muted is initialized to False
    assert reg.is_muted is False
    
    # Check that eightbit_call is a lambda function that returns its input
    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(123) == 123
    
    # Check that rgb_call is a lambda function that returns a tuple of its inputs
    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
