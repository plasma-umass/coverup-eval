# file: src/blib2to3/pgen2/token.py:80-81
# asked: {"lines": [80, 81], "branches": []}
# gained: {"lines": [80, 81], "branches": []}

import pytest
from blib2to3.pgen2.token import ISTERMINAL, NT_OFFSET

def test_ISTERMINAL_true():
    assert ISTERMINAL(NT_OFFSET - 1) == True

def test_ISTERMINAL_false():
    assert ISTERMINAL(NT_OFFSET) == False
