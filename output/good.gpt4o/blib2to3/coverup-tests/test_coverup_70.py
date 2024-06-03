# file src/blib2to3/pgen2/tokenize.py:62-63
# lines [62, 63]
# branches []

import pytest
from blib2to3.pgen2.tokenize import group

def test_group():
    # Test with no choices
    result = group()
    assert result == "()", "Expected '()', but got {}".format(result)
    
    # Test with one choice
    result = group("a")
    assert result == "(a)", "Expected '(a)', but got {}".format(result)
    
    # Test with multiple choices
    result = group("a", "b", "c")
    assert result == "(a|b|c)", "Expected '(a|b|c)', but got {}".format(result)
    
    # Test with special characters
    result = group("a", "b|c", "d")
    assert result == "(a|b|c|d)", "Expected '(a|b|c|d)', but got {}".format(result)
    
    # Test with empty string
    result = group("")
    assert result == "()", "Expected '()', but got {}".format(result)
