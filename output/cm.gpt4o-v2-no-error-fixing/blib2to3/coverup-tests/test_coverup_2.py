# file: src/blib2to3/pgen2/literals.py:58-64
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64], "branches": [[59, 0], [59, 60], [63, 59], [63, 64]]}
# gained: {"lines": [58], "branches": []}

import pytest
from blib2to3.pgen2.literals import evalString

def test_evalString():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, f"Failed at {i}: {c} != {e}"
