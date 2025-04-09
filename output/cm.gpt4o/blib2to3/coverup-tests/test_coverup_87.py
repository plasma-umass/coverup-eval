# file src/blib2to3/pgen2/pgen.py:387-425
# lines [393, 394, 395, 396, 397, 398, 401, 402, 403, 404, 407, 408, 409, 413, 414, 415, 418, 419, 420, 421, 422, 423]
# branches ['407->exit', '407->408', '408->407', '408->409', '414->415', '414->418', '418->419', '418->420', '420->421', '420->423', '421->420', '421->422']

import pytest
from blib2to3.pgen2.pgen import DFAState, NFAState

class MockNFAState(NFAState):
    pass

@pytest.fixture
def nfa_state():
    return MockNFAState()

@pytest.fixture
def dfa_state(nfa_state):
    nfaset = {nfa_state: None}
    return DFAState(nfaset, nfa_state)

def test_dfa_state_initialization(nfa_state):
    nfaset = {nfa_state: None}
    dfa_state = DFAState(nfaset, nfa_state)
    assert dfa_state.nfaset == nfaset
    assert dfa_state.isfinal is True
    assert dfa_state.arcs == {}

def test_dfa_state_addarc(dfa_state, nfa_state):
    next_state = DFAState({nfa_state: None}, nfa_state)
    label = "test_label"
    dfa_state.addarc(next_state, label)
    assert dfa_state.arcs[label] == next_state

def test_dfa_state_unifystate(dfa_state, nfa_state):
    old_state = DFAState({nfa_state: None}, nfa_state)
    new_state = DFAState({nfa_state: None}, nfa_state)
    label = "test_label"
    dfa_state.addarc(old_state, label)
    dfa_state.unifystate(old_state, new_state)
    assert dfa_state.arcs[label] == new_state

def test_dfa_state_equality(dfa_state, nfa_state):
    other_state = DFAState(dfa_state.nfaset, next(iter(dfa_state.nfaset)))
    assert dfa_state == other_state
    other_state.addarc(DFAState({nfa_state: None}, nfa_state), "different_label")
    assert dfa_state != other_state
