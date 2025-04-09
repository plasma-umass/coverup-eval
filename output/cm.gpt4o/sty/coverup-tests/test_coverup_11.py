# file sty/lib.py:20-33
# lines [20, 26, 27, 30, 31, 32, 33]
# branches ['30->exit', '30->31', '31->32', '31->33']

import pytest
from sty.lib import unmute, Register

class MockRegister(Register):
    def __init__(self):
        self.muted = True

    def unmute(self):
        self.muted = False

def test_unmute_valid_objects():
    reg1 = MockRegister()
    reg2 = MockRegister()
    
    assert reg1.muted is True
    assert reg2.muted is True
    
    unmute(reg1, reg2)
    
    assert reg1.muted is False
    assert reg2.muted is False

def test_unmute_invalid_object():
    class NotARegister:
        pass
    
    reg1 = MockRegister()
    not_a_register = NotARegister()
    
    with pytest.raises(ValueError, match=r"The unmute\(\) method can only be used with objects that inherit from the 'Register class'\."):
        unmute(reg1, not_a_register)
