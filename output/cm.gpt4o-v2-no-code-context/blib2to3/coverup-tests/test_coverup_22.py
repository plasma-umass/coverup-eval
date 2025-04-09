# file: src/blib2to3/pgen2/pgen.py:387-425
# asked: {"lines": [387, 388, 389, 390, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 406, 407, 408, 409, 411, 413, 414, 415, 418, 419, 420, 421, 422, 423, 425], "branches": [[407, 0], [407, 408], [408, 407], [408, 409], [414, 415], [414, 418], [418, 419], [418, 420], [420, 421], [420, 423], [421, 420], [421, 422]]}
# gained: {"lines": [387, 388, 389, 390, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 406, 407, 408, 409, 411, 413, 414, 418, 420, 421, 422, 423, 425], "branches": [[407, 0], [407, 408], [408, 409], [414, 418], [418, 420], [420, 421], [420, 423], [421, 420], [421, 422]]}

import pytest
from blib2to3.pgen2.pgen import DFAState, NFAState

class MockNFAState(NFAState):
    pass

@pytest.fixture
def nfa_state():
    return MockNFAState()

@pytest.fixture
def nfa_state_final():
    return MockNFAState()

@pytest.fixture
def dfa_state(nfa_state, nfa_state_final):
    return DFAState({nfa_state: None}, nfa_state_final)

@pytest.fixture
def another_dfa_state(nfa_state, nfa_state_final):
    return DFAState({nfa_state: None}, nfa_state_final)

def test_dfa_state_init(nfa_state, nfa_state_final):
    dfa_state = DFAState({nfa_state: None}, nfa_state_final)
    assert dfa_state.nfaset == {nfa_state: None}
    assert dfa_state.isfinal == (nfa_state_final in dfa_state.nfaset)
    assert dfa_state.arcs == {}

def test_dfa_state_addarc(dfa_state, another_dfa_state):
    dfa_state.addarc(another_dfa_state, 'a')
    assert dfa_state.arcs['a'] == another_dfa_state

def test_dfa_state_unifystate(dfa_state, another_dfa_state, nfa_state):
    dfa_state.addarc(another_dfa_state, 'a')
    new_dfa_state = DFAState({nfa_state: None}, nfa_state)
    dfa_state.unifystate(another_dfa_state, new_dfa_state)
    assert dfa_state.arcs['a'] == new_dfa_state

def test_dfa_state_eq(dfa_state, another_dfa_state):
    dfa_state.addarc(another_dfa_state, 'a')
    same_dfa_state = DFAState({MockNFAState(): None}, MockNFAState())
    same_dfa_state.addarc(another_dfa_state, 'a')
    assert dfa_state == same_dfa_state

def test_dfa_state_not_eq(dfa_state, another_dfa_state):
    dfa_state.addarc(another_dfa_state, 'a')
    different_dfa_state = DFAState({MockNFAState(): None}, MockNFAState())
    different_dfa_state.addarc(DFAState({MockNFAState(): None}, MockNFAState()), 'a')
    assert dfa_state != different_dfa_state
