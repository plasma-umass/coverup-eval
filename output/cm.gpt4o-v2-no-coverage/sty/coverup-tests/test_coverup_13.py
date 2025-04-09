# file: sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest
from sty.primitive import Register, Style

def test_register_unmute():
    # Create a mock Style object
    mock_style = Style()

    # Create a Register object and set attributes
    reg = Register()
    reg.is_muted = True
    reg.some_style = mock_style

    # Call unmute method
    reg.unmute()

    # Assertions to verify postconditions
    assert reg.is_muted is False
    assert reg.some_style == mock_style

    # Clean up
    del reg
    del mock_style
