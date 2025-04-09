# file: sty/lib.py:20-33
# asked: {"lines": [26, 27, 30, 31, 32, 33], "branches": [[30, 0], [30, 31], [31, 32], [31, 33]]}
# gained: {"lines": [26, 27, 30, 31, 32, 33], "branches": [[30, 0], [30, 31], [31, 32], [31, 33]]}

import pytest
from sty.lib import unmute
from sty.primitive import Register

class MockRegister(Register):
    def __init__(self):
        super().__init__()
        self.unmuted = False

    def unmute(self):
        self.unmuted = True

def test_unmute_with_valid_registers():
    reg1 = MockRegister()
    reg2 = MockRegister()
    unmute(reg1, reg2)
    assert reg1.unmuted
    assert reg2.unmuted

def test_unmute_with_invalid_register():
    class NotARegister:
        pass

    not_a_register = NotARegister()
    with pytest.raises(ValueError, match="The unmute\\(\\) method can only be used with objects that inherit from the 'Register class'."):
        unmute(not_a_register)

def test_unmute_with_mixed_valid_and_invalid_registers():
    reg = MockRegister()
    class NotARegister:
        pass

    not_a_register = NotARegister()
    with pytest.raises(ValueError, match="The unmute\\(\\) method can only be used with objects that inherit from the 'Register class'."):
        unmute(reg, not_a_register)
    assert reg.unmuted  # Ensure the valid register was unmuted even though there was an error
