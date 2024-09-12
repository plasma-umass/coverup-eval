# file: thonny/roughparse.py:638-640
# asked: {"lines": [638, 639, 640], "branches": []}
# gained: {"lines": [638, 639, 640], "branches": []}

import pytest
from thonny.roughparse import RoughParser, _closere

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "    return\n"
    parser.stmt_start = 0
    return parser

def test_is_block_closer(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2')
    assert rough_parser.is_block_closer() is True
    rough_parser._study2.assert_called_once()

    rough_parser.str = "    pass\n"
    assert rough_parser.is_block_closer() is True

    rough_parser.str = "    print('hello')\n"
    assert rough_parser.is_block_closer() is False
