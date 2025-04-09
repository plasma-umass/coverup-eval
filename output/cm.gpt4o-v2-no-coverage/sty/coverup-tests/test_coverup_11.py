# file: sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import pytest
from sty.primitive import Register, Style

class TestRegister:
    
    def test_mute(self):
        # Create a mock Style object
        style_mock = Style()
        
        # Create a Register object and set an attribute to the mock Style object
        register = Register()
        register.some_style = style_mock
        
        # Ensure the attribute is set correctly
        assert register.some_style == style_mock
        
        # Call the mute method
        register.mute()
        
        # Check that is_muted is set to True
        assert register.is_muted is True
        
        # Check that the attribute is still the same mock Style object
        assert register.some_style == style_mock
