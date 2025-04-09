# file: src/blib2to3/pgen2/pgen.py:387-425
# asked: {"lines": [415, 419], "branches": [[408, 407], [414, 415], [418, 419]]}
# gained: {"lines": [415, 419], "branches": [[414, 415], [418, 419]]}

import pytest
from blib2to3.pgen2.pgen import DFAState, NFAState

class MockNFAState(NFAState):
    pass

@pytest.fixture
def dfa_state():
    nfa_state1 = MockNFAState()
    nfa_state2 = MockNFAState()
    nfaset = {nfa_state1: None}
    return DFAState(nfaset, nfa_state1), nfa_state1, nfa_state2

def test_unifystate(dfa_state):
    state, nfa_state1, nfa_state2 = dfa_state
    new_state = DFAState({nfa_state2: None}, nfa_state2)
    state.addarc(new_state, 'a')
    assert 'a' in state.arcs
    state.unifystate(new_state, state)
    assert state.arcs['a'] is state

def test_eq_isfinal(dfa_state):
    state1, nfa_state1, nfa_state2 = dfa_state
    state2 = DFAState({nfa_state1: None}, nfa_state2)
    assert state1 != state2

def test_eq_arcs_length(dfa_state):
    state1, nfa_state1, nfa_state2 = dfa_state
    state2 = DFAState({nfa_state1: None}, nfa_state1)
    state1.addarc(state1, 'a')
    assert state1 != state2

def test_eq_arcs_content(dfa_state):
    state1, nfa_state1, nfa_state2 = dfa_state
    state2 = DFAState({nfa_state1: None}, nfa_state1)
    state1.addarc(state1, 'a')
    state2.addarc(state1, 'a')  # Ensure both states point to the same DFAState
    assert state1 == state2
    state2.addarc(state2, 'b')
    assert state1 != state2
