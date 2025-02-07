# file: sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest
from sty.primitive import Register, Style

def test_register_unmute():
    # Create a mock Style object
    mock_style = Style()

    # Create a Register object and set attributes
    register = Register()
    register.is_muted = True
    setattr(register, 'mock_style_attr', mock_style)

    # Ensure the register is muted before calling unmute
    assert register.is_muted is True

    # Call the unmute method
    register.unmute()

    # Check that the register is unmuted
    assert register.is_muted is False

    # Check that the mock_style_attr is still a Style instance
    assert isinstance(getattr(register, 'mock_style_attr'), Style)

    # Clean up
    del register
    del mock_style
