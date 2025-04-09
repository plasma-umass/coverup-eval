# file: src/blib2to3/pgen2/pgen.py:202-239
# asked: {"lines": [218, 222, 234], "branches": [[217, 218], [221, 222], [229, 228], [233, 234]]}
# gained: {"lines": [222], "branches": [[221, 222], [229, 228]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, NFAState, DFAState
from pathlib import Path
from io import StringIO

@pytest.fixture
def nfa_states():
    start = NFAState()
    mid = NFAState()
    finish = NFAState()
    start.addarc(mid, None)
    mid.addarc(finish, 'a')
    return start, finish

class DummyParserGenerator(ParserGenerator):
    def __init__(self):
        self.filename = Path("dummy")
        self.stream = StringIO("")
        self.generator = iter([])
        self.first = {}

    def parse(self):
        return {}, ""

@pytest.fixture
def parser_generator():
    return DummyParserGenerator()

def test_make_dfa(nfa_states, parser_generator):
    start, finish = nfa_states
    pg = parser_generator
    dfa_states = pg.make_dfa(start, finish)
    
    assert len(dfa_states) > 0
    assert isinstance(dfa_states[0], DFAState)
    assert dfa_states[0].isfinal == (finish in dfa_states[0].nfaset)
    
    # Check that the DFA has the correct arcs
    for state in dfa_states:
        for label, next_state in state.arcs.items():
            assert isinstance(label, str)
            assert isinstance(next_state, DFAState)
