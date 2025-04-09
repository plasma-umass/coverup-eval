# file thonny/roughparse.py:645-647
# lines [645, 646, 647]
# branches []

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def mock_study2(mocker):
    mocker.patch.object(RoughParser, '_study2', autospec=True)

def test_get_last_open_bracket_pos(mock_study2):
    parser = RoughParser(indent_width=4, tabwidth=4)  # Provide required arguments
    parser.lastopenbracketpos = 42  # Set a known state
    result = parser.get_last_open_bracket_pos()
    assert result == 42
    parser._study2.assert_called_once()
