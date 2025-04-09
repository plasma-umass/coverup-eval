# file: src/blib2to3/pgen2/tokenize.py:236-241
# asked: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}
# gained: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_add_whitespace():
    ut = Untokenizer()
    
    # Test case where row <= prev_row and col_offset is 0
    ut.prev_row = 1
    ut.prev_col = 0
    ut.add_whitespace((1, 0))
    assert ut.tokens == []

    # Test case where row <= prev_row and col_offset > 0
    ut.prev_row = 1
    ut.prev_col = 0
    ut.add_whitespace((1, 4))
    assert ut.tokens == ["    "]

    # Test case where row <= prev_row and col_offset > 0, with different values
    ut.prev_row = 2
    ut.prev_col = 2
    ut.add_whitespace((2, 5))
    assert ut.tokens == ["    ", "   "]

    # Test case where row > prev_row should raise an assertion error
    ut.prev_row = 1
    ut.prev_col = 0
    with pytest.raises(AssertionError):
        ut.add_whitespace((2, 0))
