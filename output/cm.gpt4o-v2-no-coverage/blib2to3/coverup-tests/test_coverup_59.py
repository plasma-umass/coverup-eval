# file: src/blib2to3/pgen2/tokenize.py:70-71
# asked: {"lines": [70, 71], "branches": []}
# gained: {"lines": [70, 71], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import maybe

def test_maybe_single_choice():
    result = maybe("a")
    assert result == "(a)?"

def test_maybe_multiple_choices():
    result = maybe("a", "b", "c")
    assert result == "(a|b|c)?"

def test_maybe_no_choices():
    result = maybe()
    assert result == "()?"

