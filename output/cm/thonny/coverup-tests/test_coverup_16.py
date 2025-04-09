# file thonny/roughparse.py:167-170
# lines [167, 168, 169, 170]
# branches []

import pytest
from thonny.roughparse import RoughParser

def test_set_str_with_empty_string():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.set_str("")
    assert parser.str == ""
    assert parser.study_level == 0

def test_set_str_with_newline_ending():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.set_str("print('Hello, World!')\n")
    assert parser.str == "print('Hello, World!')\n"
    assert parser.study_level == 0

def test_set_str_with_non_newline_ending():
    parser = RoughParser(indent_width=4, tabwidth=4)
    with pytest.raises(AssertionError):
        parser.set_str("This string does not end with a newline")
