# file src/blib2to3/pgen2/pgen.py:375-384
# lines [375, 376, 378, 379, 381, 382, 383, 384]
# branches []

import pytest
from blib2to3.pgen2.pgen import NFAState

def test_nfastate_addarc():
    state1 = NFAState()
    state2 = NFAState()
    
    # Test adding an arc with a label
    state1.addarc(state2, "label")
    assert state1.arcs == [("label", state2)]
    
    # Test adding an arc without a label
    state1.addarc(state2)
    assert state1.arcs == [("label", state2), (None, state2)]
    
    # Test adding an arc with None as label explicitly
    state1.addarc(state2, None)
    assert state1.arcs == [("label", state2), (None, state2), (None, state2)]

    # Test assertion for invalid label type
    with pytest.raises(AssertionError):
        state1.addarc(state2, 123)  # Invalid label type

    # Test assertion for invalid next state type
    with pytest.raises(AssertionError):
        state1.addarc("not a state", "label")  # Invalid next state type
