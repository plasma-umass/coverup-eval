# file src/blib2to3/pgen2/pgen.py:375-384
# lines [379, 382, 383, 384]
# branches []

import pytest
from blib2to3.pgen2.pgen import NFAState

def test_nfa_state_addarc_with_label():
    state1 = NFAState()
    state2 = NFAState()
    label = "test_label"
    state1.addarc(state2, label)
    assert (label, state2) in state1.arcs

def test_nfa_state_addarc_without_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2)
    assert (None, state2) in state1.arcs

def test_nfa_state_addarc_with_invalid_label(mocker):
    state1 = NFAState()
    state2 = NFAState()
    label = 123  # Not a string, should raise an assertion error
    with pytest.raises(AssertionError):
        state1.addarc(state2, label)

def test_nfa_state_addarc_with_invalid_next_state(mocker):
    state1 = NFAState()
    next_state = "not_a_state"  # Not an NFAState instance, should raise an assertion error
    with pytest.raises(AssertionError):
        state1.addarc(next_state)
