# file sty/primitive.py:158-168
# lines [158, 163, 165, 166, 167, 168]
# branches ['165->exit', '165->166', '167->165', '167->168']

import pytest
from sty import Register, Style

@pytest.fixture
def register():
    r = Register()
    r.foo = Style()
    r.bar = Style()
    # Ensure the register is not muted before each test
    r.is_muted = False
    return r

def test_register_mute(register):
    # Ensure the register is not muted before the test
    assert not register.is_muted

    # Call the mute method
    register.mute()

    # Check that the register is now muted
    assert register.is_muted

    # Check that Style attributes remain unchanged
    assert isinstance(register.foo, Style)
    assert isinstance(register.bar, Style)

    # Cleanup: reset the is_muted attribute
    register.is_muted = False
