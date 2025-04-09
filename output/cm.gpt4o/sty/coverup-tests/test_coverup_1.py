# file sty/primitive.py:195-200
# lines [195, 199, 200]
# branches []

import pytest
from collections import namedtuple
from sty.primitive import Register

class MockRegister(Register):
    def as_dict(self):
        return {'color1': 'red', 'color2': 'blue'}

def test_as_namedtuple():
    reg = MockRegister()
    nt = reg.as_namedtuple()
    
    assert isinstance(nt, tuple)
    assert nt.color1 == 'red'
    assert nt.color2 == 'blue'
    assert nt._fields == ('color1', 'color2')
