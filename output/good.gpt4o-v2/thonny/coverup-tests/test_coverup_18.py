# file: thonny/roughparse.py:632-634
# asked: {"lines": [633, 634], "branches": []}
# gained: {"lines": [633, 634], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "def foo():\n    pass\n"
    parser.goodlines = [0, 1, 2]
    parser.study_level = 1
    return parser

def test_is_block_opener(rough_parser):
    rough_parser._study2 = lambda: setattr(rough_parser, 'lastch', ':')
    assert rough_parser.is_block_opener() == True

def test_is_not_block_opener(rough_parser):
    rough_parser._study2 = lambda: setattr(rough_parser, 'lastch', 'x')
    assert rough_parser.is_block_opener() == False
