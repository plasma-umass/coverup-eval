# file sty/primitive.py:170-179
# lines [170, 174, 176, 177, 178, 179]
# branches ['176->exit', '176->177', '178->176', '178->179']

import pytest
from sty.primitive import Register, Style

class MockStyle:
    pass

@pytest.fixture
def mock_register():
    register = Register()
    register.is_muted = True
    setattr(register, 'some_style', MockStyle())
    return register

def test_unmute_register(mock_register):
    # Ensure the register is initially muted
    assert mock_register.is_muted is True
    
    # Call the unmute method
    mock_register.unmute()
    
    # Verify the register is unmuted
    assert mock_register.is_muted is False
    
    # Verify that the attribute 'some_style' is still an instance of MockStyle
    assert isinstance(mock_register.some_style, MockStyle)
