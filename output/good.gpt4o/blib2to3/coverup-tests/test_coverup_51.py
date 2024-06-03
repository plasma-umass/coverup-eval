# file src/blib2to3/pgen2/tokenize.py:225-230
# lines [225, 227, 228, 229]
# branches []

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_untokenizer_initialization():
    # Create an instance of Untokenizer
    untokenizer = Untokenizer()
    
    # Check that the tokens list is initialized correctly
    assert isinstance(untokenizer.tokens, list)
    assert len(untokenizer.tokens) == 0
    
    # Check that prev_row and prev_col are initialized correctly
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
