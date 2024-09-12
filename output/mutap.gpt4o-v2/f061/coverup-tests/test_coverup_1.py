# file: f061/__init__.py:1-11
# asked: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [1, 3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest
from f061 import correct_bracketing

def test_correct_bracketing_balanced():
    assert correct_bracketing("()") == True
    assert correct_bracketing("(())") == True
    assert correct_bracketing("()()") == True

def test_correct_bracketing_unbalanced():
    assert correct_bracketing("(()") == False
    assert correct_bracketing("())") == False
    assert correct_bracketing(")(") == False

def test_correct_bracketing_empty():
    assert correct_bracketing("") == True

def test_correct_bracketing_single_open():
    assert correct_bracketing("(") == False

def test_correct_bracketing_single_close():
    assert correct_bracketing(")") == False
