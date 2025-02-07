# file: thonny/roughparse.py:556-559
# asked: {"lines": [556, 557, 558, 559], "branches": []}
# gained: {"lines": [556, 557, 558, 559], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "def foo():\n    pass\n"
    parser.study_level = 0
    return parser

def test_get_num_lines_in_stmt(rough_parser):
    rough_parser._study1()
    rough_parser.goodlines = [0, 1, 2]
    num_lines = rough_parser.get_num_lines_in_stmt()
    assert num_lines == 1
