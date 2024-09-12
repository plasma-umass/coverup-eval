# file: sty/primitive.py:170-179
# asked: {"lines": [170, 174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [170, 174, 176, 177, 178], "branches": [[176, 0], [176, 177], [178, 176]]}

import pytest
from sty.primitive import Register, Style

class MockStyle:
    pass

@pytest.fixture
def register():
    class TestRegister(Register):
        def __init__(self):
            self.is_muted = True
            self.style_attr = MockStyle()
            self.non_style_attr = "not a style"
    return TestRegister()

def test_unmute(register):
    # Ensure initial state
    assert register.is_muted is True

    # Call the method
    register.unmute()

    # Check postconditions
    assert register.is_muted is False
    assert isinstance(register.style_attr, MockStyle)
    assert register.non_style_attr == "not a style"
