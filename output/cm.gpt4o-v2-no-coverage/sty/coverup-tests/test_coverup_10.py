# file: sty/primitive.py:195-200
# asked: {"lines": [195, 199, 200], "branches": []}
# gained: {"lines": [195, 199, 200], "branches": []}

import pytest
from collections import namedtuple
from sty.primitive import Register

@pytest.fixture
def register():
    reg = Register()
    reg.color1 = "red"
    reg.color2 = "blue"
    return reg

def test_as_namedtuple(register):
    nt = register.as_namedtuple()
    assert nt.color1 == "red"
    assert nt.color2 == "blue"
    assert isinstance(nt, tuple)
    assert hasattr(nt, '_fields')
    assert nt._fields == ('color1', 'color2')

def test_as_dict(register):
    d = register.as_dict()
    assert isinstance(d, dict)
    assert d["color1"] == "red"
    assert d["color2"] == "blue"
