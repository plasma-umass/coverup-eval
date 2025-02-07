# file: thonny/roughparse.py:236-239
# asked: {"lines": [236, 237, 238, 239], "branches": [[238, 0], [238, 239]]}
# gained: {"lines": [236, 237, 238, 239], "branches": [[238, 0], [238, 239]]}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.set_str("line1\nline2\nline3\n")
    return parser

def test_set_lo_zero(rough_parser):
    rough_parser.set_lo(0)
    assert rough_parser.str == "line1\nline2\nline3\n"

def test_set_lo_non_zero(rough_parser):
    rough_parser.set_lo(6)
    assert rough_parser.str == "line2\nline3\n"
