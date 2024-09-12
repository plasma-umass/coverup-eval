# file: src/blib2to3/pgen2/tokenize.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import any as tokenize_any

def test_tokenize_any():
    result = tokenize_any("a", "b", "c")
    assert result == "(a|b|c)*"

    result = tokenize_any("1", "2")
    assert result == "(1|2)*"

    result = tokenize_any("x")
    assert result == "(x)*"

    result = tokenize_any()
    assert result == "()*"
