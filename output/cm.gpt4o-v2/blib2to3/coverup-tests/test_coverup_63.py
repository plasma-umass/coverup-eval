# file: src/blib2to3/pgen2/tokenize.py:70-71
# asked: {"lines": [70, 71], "branches": []}
# gained: {"lines": [70, 71], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import maybe

def test_maybe():
    result = maybe("a", "b", "c")
    assert result == "(a|b|c)?"

    result = maybe("1", "2")
    assert result == "(1|2)?"

    result = maybe("x")
    assert result == "(x)?"

    result = maybe()
    assert result == "()?"

