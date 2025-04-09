# file sty/primitive.py:66-71
# lines [66, 67]
# branches []

import pytest
from sty.primitive import Register

def test_register_creation_and_usage():
    # Create a custom register
    custom_register = Register()

    # Use the register to ensure it's callable and can store values
    custom_register.foo = 'bar'
    assert custom_register.foo == 'bar'

    # Clean up by deleting the custom attribute
    del custom_register.foo
