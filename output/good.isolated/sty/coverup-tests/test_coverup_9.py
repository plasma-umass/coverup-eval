# file sty/primitive.py:170-179
# lines [170, 174, 176, 177, 178, 179]
# branches ['176->exit', '176->177', '178->176', '178->179']

import pytest
from sty.primitive import Register, Style

class MockRegister(Register):
    def __init__(self):
        super().__init__()
        self.is_muted = True
        self.some_style = Style()

@pytest.fixture
def mock_register():
    # Create a mock Register object with a Style attribute
    return MockRegister()

def test_unmute(mock_register):
    # Ensure the register is initially muted
    assert mock_register.is_muted is True
    
    # Call the unmute method
    mock_register.unmute()
    
    # Check that the register is now unmuted
    assert mock_register.is_muted is False
    
    # Check that the Style attribute remains unchanged
    assert getattr(mock_register, 'some_style') is not None
    assert isinstance(getattr(mock_register, 'some_style'), Style)
