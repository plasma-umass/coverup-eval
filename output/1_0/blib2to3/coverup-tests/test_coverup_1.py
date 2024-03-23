# file src/blib2to3/pgen2/token.py:80-81
# lines [80, 81]
# branches []

import pytest
from blib2to3.pgen2 import token

NT_OFFSET = token.NT_OFFSET

def test_ISTERMINAL():
    # Test for a terminal token (less than NT_OFFSET)
    assert token.ISTERMINAL(NT_OFFSET - 1) is True

    # Test for a non-terminal token (greater than or equal to NT_OFFSET)
    assert token.ISTERMINAL(NT_OFFSET) is False
    assert token.ISTERMINAL(NT_OFFSET + 1) is False
