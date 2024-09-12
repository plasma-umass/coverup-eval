# file: thonny/roughparse.py:645-647
# asked: {"lines": [646, 647], "branches": []}
# gained: {"lines": [646, 647], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.lastopenbracketpos = None
    return parser

def test_get_last_open_bracket_pos(rough_parser, mocker):
    mock_study2 = mocker.patch.object(rough_parser, '_study2')
    rough_parser.lastopenbracketpos = 42  # Set a test value
    result = rough_parser.get_last_open_bracket_pos()
    
    mock_study2.assert_called_once()
    assert result == 42
