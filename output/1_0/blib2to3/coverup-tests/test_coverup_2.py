# file src/blib2to3/pgen2/token.py:84-85
# lines [84, 85]
# branches []

import pytest
from blib2to3.pgen2 import token

# Assuming NT_OFFSET is a constant defined in the token module
NT_OFFSET = token.NT_OFFSET

def test_ISNONTERMINAL():
    # Test with a value below NT_OFFSET
    assert not token.ISNONTERMINAL(NT_OFFSET - 1)
    
    # Test with a value equal to NT_OFFSET
    assert token.ISNONTERMINAL(NT_OFFSET)
    
    # Test with a value above NT_OFFSET
    assert token.ISNONTERMINAL(NT_OFFSET + 1)
