# file: src/blib2to3/pgen2/token.py:88-89
# asked: {"lines": [88, 89], "branches": []}
# gained: {"lines": [88, 89], "branches": []}

import pytest
from blib2to3.pgen2.token import ISEOF, ENDMARKER

def test_ISEOF():
    assert ISEOF(ENDMARKER) is True
    assert ISEOF(999) is False
