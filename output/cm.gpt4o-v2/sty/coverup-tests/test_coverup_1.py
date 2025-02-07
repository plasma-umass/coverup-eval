# file: sty/primitive.py:202-206
# asked: {"lines": [202, 206], "branches": []}
# gained: {"lines": [202, 206], "branches": []}

import pytest
from sty.primitive import Register

def test_register_copy():
    original = Register()
    copy = original.copy()
    
    assert copy is not original
    assert isinstance(copy, Register)
    assert copy.__dict__ == original.__dict__
