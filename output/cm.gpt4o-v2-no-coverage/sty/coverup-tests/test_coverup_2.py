# file: sty/primitive.py:202-206
# asked: {"lines": [202, 206], "branches": []}
# gained: {"lines": [202, 206], "branches": []}

import pytest
from sty.primitive import Register

def test_register_copy():
    # Create an instance of Register
    original_register = Register()
    
    # Make a copy of the register
    copied_register = original_register.copy()
    
    # Assert that the copied register is indeed a deepcopy and not the same instance
    assert copied_register is not original_register
    assert copied_register.__dict__ == original_register.__dict__
