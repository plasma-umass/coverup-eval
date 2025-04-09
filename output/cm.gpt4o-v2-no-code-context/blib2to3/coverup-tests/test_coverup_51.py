# file: src/blib2to3/pgen2/tokenize.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import group

def test_group_single_choice():
    result = group("choice1")
    assert result == "(choice1)"

def test_group_multiple_choices():
    result = group("choice1", "choice2", "choice3")
    assert result == "(choice1|choice2|choice3)"
