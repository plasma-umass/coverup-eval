# file: sty/primitive.py:195-200
# asked: {"lines": [195, 199, 200], "branches": []}
# gained: {"lines": [195, 199, 200], "branches": []}

import pytest
from sty.primitive import Register

def test_as_namedtuple():
    reg = Register()
    reg.color1 = "red"
    reg.color2 = "blue"
    
    result = reg.as_namedtuple()
    
    assert result.color1 == "red"
    assert result.color2 == "blue"
    
    del reg.color1
    del reg.color2
