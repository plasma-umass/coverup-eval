# file src/blib2to3/pgen2/tokenize.py:66-67
# lines [66, 67]
# branches []

import pytest
from blib2to3.pgen2.tokenize import group

def test_any_function():
    def any(*choices):
        return group(*choices) + "*"

    # Test with no choices
    result = any()
    assert result == "()*"

    # Test with one choice
    result = any("a")
    assert result == "(a)*"

    # Test with multiple choices
    result = any("a", "b", "c")
    assert result == "(a|b|c)*"
