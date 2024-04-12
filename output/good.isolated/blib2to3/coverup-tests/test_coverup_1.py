# file src/blib2to3/pgen2/literals.py:58-64
# lines [58, 59, 60, 61, 62, 63, 64]
# branches ['59->exit', '59->60', '63->59', '63->64']

import pytest
from blib2to3.pgen2.literals import evalString

@pytest.fixture(scope="module")
def cleanup():
    # Setup if necessary
    yield
    # Cleanup code if necessary

def test_evalString_full_coverage(cleanup):
    # Test all 256 characters to ensure full coverage
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, f"Failed at char {i}: {c}, {s}, {e}"
