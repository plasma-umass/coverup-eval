# file src/blib2to3/pgen2/token.py:88-89
# lines [88, 89]
# branches []

import pytest
from blib2to3.pgen2 import token

def test_ISEOF():
    assert token.ISEOF(token.ENDMARKER) == True
    # Assuming that ENDMARKER is not 0, the following test should be corrected
    assert token.ISEOF(0) == (0 == token.ENDMARKER)
    assert token.ISEOF(1) == False
    assert token.ISEOF(-1) == False
    assert token.ISEOF(token.ENDMARKER + 1) == False
