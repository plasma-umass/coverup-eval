# file src/blib2to3/pgen2/tokenize.py:62-63
# lines [62, 63]
# branches []

import pytest
from blib2to3.pgen2 import tokenize

def test_group_function():
    # Test the group function with multiple choices
    result = tokenize.group("a", "b", "c")
    assert result == "(a|b|c)"

    # Test the group function with a single choice
    result = tokenize.group("onlyone")
    assert result == "(onlyone)"

    # Test the group function with no choices
    result = tokenize.group()
    assert result == "()"
