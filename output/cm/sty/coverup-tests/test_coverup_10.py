# file sty/primitive.py:202-206
# lines [202, 206]
# branches []

import pytest
from sty.primitive import Register
from copy import deepcopy

def test_register_copy():
    # Create a Register instance and make a copy
    original_register = Register()
    copied_register = original_register.copy()

    # Assert that the copied register is not the same object as the original
    assert copied_register is not original_register

    # Assert that the copied register is an instance of Register
    assert isinstance(copied_register, Register)

    # Assert that the copied register is a deepcopy of the original
    assert copied_register.__dict__ == original_register.__dict__
