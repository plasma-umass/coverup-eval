# file: src/blib2to3/pgen2/token.py:84-85
# asked: {"lines": [84, 85], "branches": []}
# gained: {"lines": [84, 85], "branches": []}

import pytest
from blib2to3.pgen2.token import ISNONTERMINAL, NT_OFFSET

def test_ISNONTERMINAL():
    assert ISNONTERMINAL(NT_OFFSET) == True
    assert ISNONTERMINAL(NT_OFFSET - 1) == False
