# file: src/blib2to3/pgen2/tokenize.py:231-234
# asked: {"lines": [231, 232, 233, 234], "branches": []}
# gained: {"lines": [231, 232, 233, 234], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_untokenizer_initialization():
    # Create an instance of Untokenizer
    ut = Untokenizer()
    
    # Assert that the tokens list is initialized empty
    assert ut.tokens == []
    
    # Assert that prev_row is initialized to 1
    assert ut.prev_row == 1
    
    # Assert that prev_col is initialized to 0
    assert ut.prev_col == 0
