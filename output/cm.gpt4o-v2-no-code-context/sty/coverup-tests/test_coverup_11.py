# file: sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178], "branches": [[176, 0], [176, 177], [178, 176]]}

import pytest
from sty.primitive import Register, Style

class MockStyle:
    pass

@pytest.fixture
def register():
    reg = Register()
    reg.is_muted = True
    reg.style_attr = MockStyle()
    return reg

def test_unmute(register):
    assert register.is_muted is True
    register.unmute()
    assert register.is_muted is False
    assert isinstance(register.style_attr, MockStyle)
