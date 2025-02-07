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
    
    assert reg1.unmuted is True
    assert reg2.unmuted is True

def test_unmute_with_invalid_register():
    class NotARegister:
        pass
    
    reg1 = MockRegister()
    not_a_reg = NotARegister()
    
    with pytest.raises(ValueError, match="The unmute\\(\\) method can only be used with objects that inherit from the 'Register class'."):
        unmute(reg1, not_a_reg)
