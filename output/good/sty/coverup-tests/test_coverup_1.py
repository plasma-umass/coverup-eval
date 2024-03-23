# file sty/lib.py:20-33
# lines [20, 26, 27, 30, 31, 32, 33]
# branches ['30->exit', '30->31', '31->32', '31->33']

import pytest
from sty import Register, unmute

class MockRegister(Register):
    def __init__(self):
        self.muted = True

    def unmute(self):
        self.muted = False

@pytest.fixture
def mock_register():
    return MockRegister()

def test_unmute_with_valid_registers(mock_register):
    assert mock_register.muted is True
    unmute(mock_register)
    assert mock_register.muted is False

def test_unmute_with_invalid_object():
    with pytest.raises(ValueError):
        unmute(object())
