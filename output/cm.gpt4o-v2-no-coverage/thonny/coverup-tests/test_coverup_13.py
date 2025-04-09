# file: thonny/roughparse.py:654-656
# asked: {"lines": [654, 655, 656], "branches": []}
# gained: {"lines": [654, 655, 656], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.study_level = 0
    parser.str = ""
    parser.goodlines = []
    parser.stmt_bracketing = None
    return parser

def test_get_last_stmt_bracketing(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2', autospec=True)
    rough_parser.stmt_bracketing = (1, 2, 3)
    
    result = rough_parser.get_last_stmt_bracketing()
    
    rough_parser._study2.assert_called_once()
    assert result == (1, 2, 3)
