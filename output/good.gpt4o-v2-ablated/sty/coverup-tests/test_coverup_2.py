# file: sty/primitive.py:158-168
# asked: {"lines": [158, 163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [158, 163, 165, 166, 167], "branches": [[165, 0], [165, 166], [167, 165]]}

import pytest
from sty.primitive import Register, Style

class MockStyle:
    pass

@pytest.fixture
def register():
    class TestRegister(Register):
        def __init__(self):
            self.is_muted = False
            self.style_attr = MockStyle()
            self.non_style_attr = "not a style"
    return TestRegister()

def test_mute(register):
    assert not register.is_muted
    register.mute()
    assert register.is_muted
    assert isinstance(register.style_attr, MockStyle)
    assert register.non_style_attr == "not a style"
