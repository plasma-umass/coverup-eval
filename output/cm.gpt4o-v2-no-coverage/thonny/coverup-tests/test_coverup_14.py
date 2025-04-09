# file: thonny/roughparse.py:167-170
# asked: {"lines": [167, 168, 169, 170], "branches": []}
# gained: {"lines": [167, 168, 169, 170], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def parser():
    return RoughParser(indent_width=4, tabwidth=4)

def test_set_str_empty_string(parser):
    parser.set_str("")
    assert parser.str == ""
    assert parser.study_level == 0

def test_set_str_newline_string(parser):
    parser.set_str("\n")
    assert parser.str == "\n"
    assert parser.study_level == 0

def test_set_str_invalid_string(parser):
    with pytest.raises(AssertionError):
        parser.set_str("invalid")
