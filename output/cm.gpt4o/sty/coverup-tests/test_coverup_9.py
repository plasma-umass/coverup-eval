# file sty/lib.py:4-17
# lines [4, 10, 11, 14, 15, 16, 17]
# branches ['14->exit', '14->15', '15->16', '15->17']

import pytest
from sty.lib import mute, Register

class MockRegister(Register):
    def __init__(self):
        self.muted = False

    def mute(self):
        self.muted = True

def test_mute_multiple_registers():
    reg1 = MockRegister()
    reg2 = MockRegister()
    mute(reg1, reg2)
    assert reg1.muted
    assert reg2.muted

def test_mute_with_non_register():
    class NonRegister:
        pass

    reg1 = MockRegister()
    non_reg = NonRegister()
    
    with pytest.raises(ValueError, match=r"The mute\(\) method can only be used with objects that inherit from the 'Register class'\."):
        mute(reg1, non_reg)
