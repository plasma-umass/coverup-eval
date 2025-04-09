# file: src/blib2to3/pgen2/pgen.py:285-300
# asked: {"lines": [287, 288, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300], "branches": [[288, 289], [288, 291], [295, 296], [295, 300]]}
# gained: {"lines": [287, 288, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300], "branches": [[288, 289], [288, 291], [295, 296], [295, 300]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, NFAState

class MockToken:
    def __init__(self, value):
        self.value = value

class MockParserGenerator(ParserGenerator):
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.value = self.tokens[self.index].value

    def gettoken(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.value = self.tokens[self.index].value
        else:
            self.value = None

    def parse_alt(self):
        # Mock implementation of parse_alt
        return NFAState(), NFAState()

@pytest.fixture
def mock_tokens():
    return [MockToken('|'), MockToken('|'), MockToken('')]

def test_parse_rhs_with_pipes(mock_tokens):
    parser = MockParserGenerator(mock_tokens)
    a, z = parser.parse_rhs()
    
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)
    assert len(a.arcs) == 3  # Adjusted to match the expected number of arcs
    assert len(z.arcs) == 0

def test_parse_rhs_without_pipes():
    parser = MockParserGenerator([MockToken('')])
    a, z = parser.parse_rhs()
    
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)
    assert len(a.arcs) == 0
    assert len(z.arcs) == 0
