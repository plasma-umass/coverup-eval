# file: src/blib2to3/pgen2/tokenize.py:236-241
# asked: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}
# gained: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

@pytest.fixture
def untokenizer():
    return Untokenizer()

def test_add_whitespace_no_offset(untokenizer):
    untokenizer.prev_row = 1
    untokenizer.prev_col = 0
    untokenizer.add_whitespace((1, 0))
    assert untokenizer.tokens == []

def test_add_whitespace_with_offset(untokenizer):
    untokenizer.prev_row = 1
    untokenizer.prev_col = 0
    untokenizer.add_whitespace((1, 4))
    assert untokenizer.tokens == ["    "]

def test_add_whitespace_assertion(untokenizer):
    untokenizer.prev_row = 2
    untokenizer.prev_col = 0
    with pytest.raises(AssertionError):
        untokenizer.add_whitespace((3, 0))
