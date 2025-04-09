# file: thonny/roughparse.py:621-628
# asked: {"lines": [622, 623, 624, 625, 626, 627, 628], "branches": [[626, 627], [626, 628]]}
# gained: {"lines": [622, 623, 624, 625, 626, 627, 628], "branches": [[626, 627], [626, 628]]}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.stmt_start = 0
    parser.stmt_end = 10
    parser.str = "    some code"
    return parser

def test_get_base_indent_string(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2')
    result = rough_parser.get_base_indent_string()
    assert result == "    "
    rough_parser._study2.assert_called_once()
