# file sty/lib.py:4-17
# lines [4, 10, 11, 14, 15, 16, 17]
# branches ['14->exit', '14->15', '15->16', '15->17']

import pytest
from sty import Register, lib

class MockRegister(Register):
    def __init__(self):
        self.muted = False

    def mute(self):
        self.muted = True

@pytest.fixture
def mock_register():
    return MockRegister()

def test_mute_with_valid_registers(mock_register):
    lib.mute(mock_register, mock_register)
    assert mock_register.muted

def test_mute_with_invalid_object(mock_register):
    with pytest.raises(ValueError) as exc_info:
        lib.mute(mock_register, "not a register object")
    assert "from the 'Register class'" in str(exc_info.value)
