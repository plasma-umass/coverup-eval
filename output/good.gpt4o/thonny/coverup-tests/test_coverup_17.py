# file thonny/roughparse.py:236-239
# lines [236, 237, 238, 239]
# branches ['238->exit', '238->239']

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "\nexample\ntext\n"
    return parser

def test_set_lo_zero(rough_parser):
    rough_parser.set_lo(0)
    assert rough_parser.str == "\nexample\ntext\n"

def test_set_lo_non_zero(rough_parser):
    rough_parser.set_lo(1)
    assert rough_parser.str == "example\ntext\n"

def test_set_lo_non_zero_with_newline(rough_parser):
    rough_parser.str = "\nexample\ntext\n"
    rough_parser.set_lo(9)
    assert rough_parser.str == "text\n"

def test_set_lo_assertion_error(rough_parser):
    with pytest.raises(AssertionError):
        rough_parser.set_lo(2)
