# file src/blib2to3/pgen2/tokenize.py:236-241
# lines [236, 237, 238, 239, 240, 241]
# branches ['240->exit', '240->241']

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

@pytest.fixture
def untokenizer():
    ut = Untokenizer()
    ut.tokens = []
    ut.prev_row, ut.prev_col = 1, 0  # Initialize to the start of a file
    return ut

def test_add_whitespace_same_row(untokenizer):
    # Test adding whitespace on the same row
    untokenizer.add_whitespace((1, 5))
    assert untokenizer.tokens == ['     '], "Whitespace should be added"

def test_add_whitespace_no_col_offset(untokenizer):
    # Test adding no whitespace if col_offset is 0
    untokenizer.add_whitespace((1, 0))
    assert untokenizer.tokens == [], "No whitespace should be added if col_offset is 0"

def test_add_whitespace_assertion_error(untokenizer):
    # Test that an AssertionError is raised if row > prev_row
    with pytest.raises(AssertionError):
        untokenizer.add_whitespace((2, 0))

# Clean up is handled by the fixture, no top-level code is needed.
