# file: src/blib2to3/pgen2/pgen.py:55-78
# asked: {"lines": [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[61, 62], [61, 65], [65, 66], [65, 77], [68, 69], [68, 75], [70, 71], [70, 72], [72, 73], [72, 74]]}
# gained: {"lines": [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[61, 62], [61, 65], [65, 66], [65, 77], [68, 69], [68, 75], [70, 71], [70, 72], [72, 73], [72, 74]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar

class MockDFAState:
    def __init__(self, arcs, isfinal=False):
        self.arcs = arcs
        self.isfinal = isfinal

class MockParserGenerator(ParserGenerator):
    def __init__(self, dfas, startsymbol, first):
        self.dfas = dfas
        self.startsymbol = startsymbol
        self.first = first

    def make_label(self, c, label):
        return super().make_label(c, label)

    def make_first(self, c, name):
        return super().make_first(c, name)

@pytest.fixture
def mock_pgen_grammar():
    return PgenGrammar()

@pytest.fixture
def mock_parser_generator():
    state_b = MockDFAState({}, True)
    state_a = MockDFAState({'b': state_b}, False)
    state_start = MockDFAState({'a': state_a}, True)
    
    dfas = {
        'start': [state_start, state_a, state_b],
        'a': [state_a, state_b],
        'b': [state_b]
    }
    startsymbol = 'start'
    first = {
        'start': {'a'},
        'a': {'b'},
        'b': set()
    }
    return MockParserGenerator(dfas, startsymbol, first)

def test_make_grammar(mock_parser_generator, mock_pgen_grammar):
    c = mock_parser_generator.make_grammar()
    
    # Assertions to verify the grammar creation
    assert c.start == 256
    assert c.symbol2number == {'start': 256, 'a': 257, 'b': 258}
    assert c.number2symbol == {256: 'start', 257: 'a', 258: 'b'}
    assert len(c.states) == 3
    assert len(c.dfas) == 3
    assert c.dfas[256][1] == {mock_parser_generator.make_label(c, 'a'): 1}
    assert c.dfas[257][1] == {mock_parser_generator.make_label(c, 'b'): 1}
    assert c.dfas[258][1] == {}

