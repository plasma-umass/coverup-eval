# file: sty/primitive.py:158-168
# asked: {"lines": [158, 163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [158, 163, 165, 166, 167], "branches": [[165, 0], [165, 166], [167, 165]]}

import pytest
from sty.primitive import Register, Style

class TestRegister:
    def test_mute(self):
        # Create a mock Style object
        class MockStyle:
            pass

        # Create a Register object and set attributes
        register = Register()
        register.style1 = MockStyle()
        register.style2 = MockStyle()
        register.non_style = "not a style"

        # Ensure initial state
        assert not getattr(register, 'is_muted', False)

        # Call the mute method
        register.mute()

        # Check postconditions
        assert register.is_muted is True
        assert isinstance(register.style1, MockStyle)
        assert isinstance(register.style2, MockStyle)
        assert register.non_style == "not a style"
