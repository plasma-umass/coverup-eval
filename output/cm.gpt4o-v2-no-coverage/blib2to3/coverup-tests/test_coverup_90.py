# file: src/blib2to3/pgen2/parse.py:205-217
# asked: {"lines": [209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215], [214, 217]]}
# gained: {"lines": [209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215]]}

import pytest
from blib2to3.pytree import Context, RawNode
from blib2to3.pgen2.parse import Parser

@pytest.fixture
def parser():
    class MockGrammar:
        pass

    class MockParser(Parser):
        def __init__(self):
            self.stack = [("dfa", "state", [[]])]
            self.grammar = MockGrammar()

        def convert(self, grammar, rawnode):
            return rawnode  # Simplified for testing

    return MockParser()

def test_shift(parser):
    type = 1
    value = "value"
    newstate = 2
    context = ("context", (1, 2))

    parser.shift(type, value, newstate, context)

    dfa, state, node = parser.stack[-1]
    assert dfa == "dfa"
    assert state == newstate
    assert node == [[(type, value, context, None)]]
