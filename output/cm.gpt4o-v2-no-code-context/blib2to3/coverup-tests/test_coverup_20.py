# file: src/blib2to3/pgen2/pgen.py:375-384
# asked: {"lines": [375, 376, 378, 379, 381, 382, 383, 384], "branches": []}
# gained: {"lines": [375, 376, 378, 379, 381, 382, 383, 384], "branches": []}

import pytest
from blib2to3.pgen2.pgen import NFAState

def test_nfastate_initialization():
    state = NFAState()
    assert state.arcs == []

def test_nfastate_addarc_with_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2, "label")
    assert state1.arcs == [("label", state2)]

def test_nfastate_addarc_without_label():
    state1 = NFAState()
    state2 = NFAState()
    state1.addarc(state2)
    assert state1.arcs == [(None, state2)]

def test_nfastate_addarc_invalid_label():
    state1 = NFAState()
    state2 = NFAState()
    with pytest.raises(AssertionError):
        state1.addarc(state2, 123)  # Invalid label, should raise AssertionError

def test_nfastate_addarc_invalid_next_state():
    state1 = NFAState()
    with pytest.raises(AssertionError):
        state1.addarc("not_a_state")  # Invalid next state, should raise AssertionError
