# file: sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import pytest
from sty.primitive import Register, Style

def test_register_mute(monkeypatch):
    # Create a mock Style instance
    mock_style = Style()

    # Create a Register instance and set an attribute to the mock Style
    register = Register()
    setattr(register, 'mock_style_attr', mock_style)

    # Ensure the attribute is set correctly
    assert getattr(register, 'mock_style_attr') == mock_style

    # Mute the register
    register.mute()

    # Check if the register is muted
    assert register.is_muted

    # Check if the attribute remains unchanged
    assert getattr(register, 'mock_style_attr') == mock_style

    # Clean up by unmuting the register
    register.is_muted = False
    delattr(register, 'mock_style_attr')
