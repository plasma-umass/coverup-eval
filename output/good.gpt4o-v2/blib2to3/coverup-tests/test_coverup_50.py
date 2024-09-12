# file: src/blib2to3/pgen2/pgen.py:202-239
# asked: {"lines": [202, 207, 208, 210, 211, 212, 213, 215, 216, 217, 218, 219, 220, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 236, 237, 238, 239], "branches": [[217, 218], [217, 219], [220, 0], [220, 221], [221, 220], [221, 222], [225, 226], [225, 239], [227, 228], [227, 231], [228, 227], [228, 229], [229, 228], [229, 230], [231, 225], [231, 232], [232, 233], [232, 236], [233, 232], [233, 234]]}
# gained: {"lines": [202, 207, 208, 210, 211, 212, 213, 215, 216, 217, 219, 220, 221, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 236, 237, 238, 239], "branches": [[217, 219], [220, 0], [220, 221], [221, 220], [225, 226], [225, 239], [227, 228], [227, 231], [228, 227], [228, 229], [229, 230], [231, 225], [231, 232], [232, 233], [232, 236], [233, 232]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2.pgen import NFAState, DFAState
from io import StringIO

@pytest.fixture
def nfa_states():
    start = NFAState()
    finish = NFAState()
    return start, finish

@pytest.fixture
def parser_generator(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, 'dummy_start'))
    dummy_stream = StringIO("")
    pg = ParserGenerator("dummy_path", dummy_stream)
    yield pg
    dummy_stream.close()

def test_make_dfa(nfa_states, parser_generator):
    start, finish = nfa_states
    pg = parser_generator

    # Create a simple NFA
    mid = NFAState()
    start.addarc(mid, 'a')
    mid.addarc(finish, 'b')

    # Generate DFA from NFA
    dfa_states = pg.make_dfa(start, finish)

    # Assertions to verify DFA creation
    assert len(dfa_states) > 0
    assert isinstance(dfa_states[0], DFAState)
    assert dfa_states[0].isfinal == False
    assert any(state.isfinal for state in dfa_states)

    # Clean up
    del pg
    del start
    del finish
    del mid
    del dfa_states
