# file thonny/roughparse.py:654-656
# lines [654, 655, 656]
# branches []

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def mock_study2(mocker):
    return mocker.patch.object(RoughParser, '_study2')

def test_get_last_stmt_bracketing(mock_study2):
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.stmt_bracketing = "test_bracketing"
    
    result = parser.get_last_stmt_bracketing()
    
    mock_study2.assert_called_once()
    assert result == "test_bracketing"
