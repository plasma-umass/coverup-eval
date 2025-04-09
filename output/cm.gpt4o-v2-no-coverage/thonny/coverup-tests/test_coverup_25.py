# file: thonny/roughparse.py:632-634
# asked: {"lines": [633, 634], "branches": []}
# gained: {"lines": [633, 634], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.study_level = 0
    parser.str = ""
    parser.goodlines = []
    return parser

def test_is_block_opener_colon(rough_parser, mocker):
    mocker.patch.object(rough_parser, 'str', "def foo():\n    pass\n")
    mocker.patch.object(rough_parser, 'goodlines', [0, 1, 2])
    rough_parser._study2()
    rough_parser.lastch = ":"
    assert rough_parser.is_block_opener() == True

def test_is_block_opener_no_colon(rough_parser, mocker):
    mocker.patch.object(rough_parser, 'str', "def foo()\n    pass\n")
    mocker.patch.object(rough_parser, 'goodlines', [0, 1, 2])
    rough_parser._study2()
    rough_parser.lastch = ""
    assert rough_parser.is_block_opener() == False
