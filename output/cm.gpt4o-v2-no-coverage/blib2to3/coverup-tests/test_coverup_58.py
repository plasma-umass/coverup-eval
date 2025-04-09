# file: src/blib2to3/pgen2/tokenize.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import any as tokenize_any

def test_any_with_choices():
    result = tokenize_any("a", "b", "c")
    assert result == "(a|b|c)*"

def test_any_with_no_choices():
    result = tokenize_any()
    assert result == "()*"
