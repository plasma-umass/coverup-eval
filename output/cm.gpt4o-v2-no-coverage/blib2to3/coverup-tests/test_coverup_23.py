# file: src/blib2to3/pgen2/pgen.py:375-384
# asked: {"lines": [375, 376, 378, 379, 381, 382, 383, 384], "branches": []}
# gained: {"lines": [375, 376, 378, 379, 381, 382, 383, 384], "branches": []}

import pytest
from blib2to3.pgen2.pgen import NFAState

def test_nfastate_init():
    state = NFAState()
    assert state.arcs == []

def test_nfastate_addarc():
    state1 = NFAState()
    state2 = NFAState()
    
    state1.addarc(state2, "a")
    assert state1.arcs == [("a", state2)]
    
    state3 = NFAState()
    state1.addarc(state3)
    assert state1.arcs == [("a", state2), (None, state3)]

    with pytest.raises(AssertionError):
        state1.addarc(state2, 123)  # Invalid label type

    with pytest.raises(AssertionError):
        state1.addarc("not a state")  # Invalid next state type
