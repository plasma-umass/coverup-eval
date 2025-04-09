# file thonny/roughparse.py:167-170
# lines [167, 168, 169, 170]
# branches []

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    return RoughParser(indent_width=4, tabwidth=4)

def test_set_str_empty_string(rough_parser):
    rough_parser.set_str("")
    assert rough_parser.str == ""
    assert rough_parser.study_level == 0

def test_set_str_newline_string(rough_parser):
    rough_parser.set_str("test\n")
    assert rough_parser.str == "test\n"
    assert rough_parser.study_level == 0

def test_set_str_no_newline_string(rough_parser):
    with pytest.raises(AssertionError):
        rough_parser.set_str("test")
