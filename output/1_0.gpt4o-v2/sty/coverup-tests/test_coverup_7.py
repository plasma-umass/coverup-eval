# file: sty/renderfunc.py:9-10
# asked: {"lines": [9, 10], "branches": []}
# gained: {"lines": [9, 10], "branches": []}

import pytest
from sty.renderfunc import sgr

def test_sgr():
    # Test with a sample integer
    result = sgr(31)
    assert result == '\x1b[31m'

    # Test with another integer
    result = sgr(0)
    assert result == '\x1b[0m'

    # Test with a larger integer
    result = sgr(123)
    assert result == '\x1b[123m'
