# file: src/blib2to3/pgen2/tokenize.py:236-241
# asked: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}
# gained: {"lines": [236, 237, 238, 239, 240, 241], "branches": [[240, 0], [240, 241]]}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

@pytest.fixture
def untokenizer():
    class MockUntokenizer(Untokenizer):
        def __init__(self):
            self.tokens = []
            self.prev_row = 0
            self.prev_col = 0

    return MockUntokenizer()

def test_add_whitespace_no_offset(untokenizer):
    untokenizer.prev_row = 1
    untokenizer.prev_col = 5
    untokenizer.add_whitespace((1, 5))
    assert untokenizer.tokens == []

def test_add_whitespace_with_offset(untokenizer):
    untokenizer.prev_row = 1
    untokenizer.prev_col = 3
    untokenizer.add_whitespace((1, 5))
    assert untokenizer.tokens == ["  "]

def test_add_whitespace_new_row(untokenizer):
    untokenizer.prev_row = 2
    untokenizer.prev_col = 5
    with pytest.raises(AssertionError):
        untokenizer.add_whitespace((3, 5))
