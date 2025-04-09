# file src/blib2to3/pgen2/tokenize.py:236-241
# lines []
# branches ['240->exit']

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_add_whitespace_executes_branch_240(mocker):
    # Mocking the initial state of the Untokenizer instance
    untokenizer = Untokenizer()
    untokenizer.prev_row = 1
    untokenizer.prev_col = 2
    untokenizer.tokens = []

    # Mocking the start coordinate to trigger the branch
    start = (1, 2)

    # Call the method
    untokenizer.add_whitespace(start)

    # Assertions to verify the postconditions
    assert untokenizer.tokens == []

    # Clean up
    del untokenizer
