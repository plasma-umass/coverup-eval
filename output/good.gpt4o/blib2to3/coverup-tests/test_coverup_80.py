# file src/blib2to3/pgen2/tokenize.py:236-241
# lines [237, 238, 239, 240, 241]
# branches ['240->exit', '240->241']

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

@pytest.fixture
def untokenizer():
    class MockUntokenizer(Untokenizer):
        def __init__(self):
            self.prev_row = 1
            self.prev_col = 0
            self.tokens = []

    return MockUntokenizer()

def test_add_whitespace_executes_missing_lines(untokenizer):
    # Set up the initial state
    untokenizer.prev_row = 1
    untokenizer.prev_col = 0

    # Call the method with a start coordinate that will trigger the missing lines
    start_coord = (1, 4)
    untokenizer.add_whitespace(start_coord)

    # Assertions to verify the postconditions
    assert untokenizer.tokens == ["    "]
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
