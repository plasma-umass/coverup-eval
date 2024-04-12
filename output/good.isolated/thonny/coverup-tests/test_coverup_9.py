# file thonny/roughparse.py:236-239
# lines [236, 237, 238, 239]
# branches ['238->exit', '238->239']

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    rp = RoughParser(indent_width=4, tabwidth=4)
    rp.str = "test\nstring"
    return rp

def test_set_lo_with_newline(rough_parser):
    rough_parser.set_lo(5)
    assert rough_parser.str == "string"

def test_set_lo_with_zero(rough_parser):
    rough_parser.set_lo(0)
    assert rough_parser.str == "test\nstring"

def test_set_lo_with_invalid_lo(rough_parser):
    with pytest.raises(AssertionError):
        rough_parser.set_lo(3)  # This should raise an AssertionError
