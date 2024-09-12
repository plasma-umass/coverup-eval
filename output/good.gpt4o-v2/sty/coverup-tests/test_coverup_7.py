# file: sty/lib.py:4-17
# asked: {"lines": [4, 10, 11, 14, 15, 16, 17], "branches": [[14, 0], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [4, 10, 11, 14, 15, 16, 17], "branches": [[14, 0], [14, 15], [15, 16], [15, 17]]}

import pytest
from sty.lib import mute
from sty.primitive import Register

class CustomRegister(Register):
    def __init__(self):
        super().__init__()
        self.muted = False

    def mute(self):
        self.muted = True

def test_mute_with_valid_register():
    reg1 = CustomRegister()
    reg2 = CustomRegister()
    
    mute(reg1, reg2)
    
    assert reg1.muted is True
    assert reg2.muted is True

def test_mute_with_invalid_register():
    class NotARegister:
        pass
    
    reg1 = CustomRegister()
    not_a_reg = NotARegister()
    
    with pytest.raises(ValueError, match="The mute\\(\\) method can only be used with objects that inherit from the 'Register class'."):
        mute(reg1, not_a_reg)
