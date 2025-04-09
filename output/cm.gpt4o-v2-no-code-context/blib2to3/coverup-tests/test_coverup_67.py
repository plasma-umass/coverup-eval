# file: src/blib2to3/pgen2/tokenize.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_any_function():
    from blib2to3.pgen2.tokenize import any as any_function

    # Test with no arguments
    result = any_function()
    assert result == "()*"

    # Test with one argument
    result = any_function("a")
    assert result == "(a)*"

    # Test with multiple arguments
    result = any_function("a", "b", "c")
    assert result == "(a|b|c)*"
