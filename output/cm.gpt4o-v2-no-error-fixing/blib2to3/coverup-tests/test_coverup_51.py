# file: src/blib2to3/pgen2/tokenize.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import any as any_choices
from blib2to3.pgen2.tokenize import group

def test_any_function():
    # Test with no choices
    result = any_choices()
    assert result == "()*"

    # Test with one choice
    result = any_choices("a")
    assert result == "(a)*"

    # Test with multiple choices
    result = any_choices("a", "b", "c")
    assert result == "(a|b|c)*"

    # Clean up if necessary (not needed in this case as there is no state change)

def test_group_function():
    # Test with no choices
    result = group()
    assert result == "()"

    # Test with one choice
    result = group("a")
    assert result == "(a)"

    # Test with multiple choices
    result = group("a", "b", "c")
    assert result == "(a|b|c)"

    # Clean up if necessary (not needed in this case as there is no state change)
