# file sty/primitive.py:202-206
# lines [202, 206]
# branches []

import pytest
from sty.primitive import Register
from unittest.mock import patch
from copy import deepcopy

def test_register_copy(mocker):
    # Create an instance of Register
    register = Register()
    
    # Mock deepcopy to ensure it is called
    mock_deepcopy = mocker.patch('sty.primitive.deepcopy', wraps=deepcopy)
    
    # Call the copy method
    copied_register = register.copy()
    
    # Assert deepcopy was called with the register instance
    mock_deepcopy.assert_called_once_with(register)
    
    # Assert the returned object is a deepcopy of the original
    assert copied_register is not register
    assert isinstance(copied_register, Register)
