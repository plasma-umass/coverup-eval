# file sty/primitive.py:195-200
# lines [195, 199, 200]
# branches []

import pytest
from sty.primitive import Register
from collections import namedtuple

def test_as_namedtuple():
    # Setup
    register = Register()
    register.foo = 'bar'
    register.baz = 'qux'

    # Exercise
    StyleRegister = register.as_namedtuple()

    # Verify
    assert isinstance(StyleRegister, tuple)
    assert StyleRegister.foo == 'bar'
    assert StyleRegister.baz == 'qux'

    # Cleanup - nothing to clean up as no external resources or state changes were made
