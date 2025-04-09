# file: src/blib2to3/pgen2/tokenize.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_group_single_choice():
    assert group("a") == "(a)"

def test_group_multiple_choices():
    assert group("a", "b", "c") == "(a|b|c)"

def test_group_no_choices():
    assert group() == "()"
