# file: src/blib2to3/pgen2/parse.py:205-217
# asked: {"lines": [209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215], [214, 217]]}
# gained: {"lines": [209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215], [214, 217]]}

import pytest
from blib2to3.pytree import Context
from blib2to3.pgen2.parse import Parser

@pytest.fixture
def parser():
    class MockGrammar:
        pass

    class MockParser(Parser):
        def __init__(self):
            self.stack = [(None, None, [[]])]
            self.grammar = MockGrammar()

        def convert(self, grammar, rawnode):
            return rawnode  # Mock conversion for testing

    return MockParser()

def test_shift_executes_all_branches(parser):
    type = 1
    value = "test"
    newstate = 2
    context = ("test_context", (1, 2))

    parser.shift(type, value, newstate, context)

    # Assertions to verify postconditions
    assert parser.stack[-1][1] == newstate
    assert parser.stack[-1][2][-1][-1] == (type, value, context, None)

def test_shift_with_none_newnode(parser):
    type = 1
    value = "test"
    newstate = 2
    context = ("test_context", (1, 2))

    # Mock convert to return None
    def mock_convert(grammar, rawnode):
        return None

    parser.convert = mock_convert

    parser.shift(type, value, newstate, context)

    # Assertions to verify postconditions
    assert parser.stack[-1][1] == newstate
    assert parser.stack[-1][2][-1] == []

