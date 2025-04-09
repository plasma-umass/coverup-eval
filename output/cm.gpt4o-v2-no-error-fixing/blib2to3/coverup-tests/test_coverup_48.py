# file: src/blib2to3/pgen2/tokenize.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_group():
    # Test with no choices
    assert group() == "()"
    
    # Test with one choice
    assert group("a") == "(a)"
    
    # Test with multiple choices
    assert group("a", "b", "c") == "(a|b|c)"
