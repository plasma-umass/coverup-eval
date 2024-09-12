# file: sty/renderfunc.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest
from sty.renderfunc import eightbit_bg

def test_eightbit_bg():
    # Test with a sample input
    result = eightbit_bg(42)
    assert result == '\x1b[48;5;42m'
    
    # Test with another input
    result = eightbit_bg(0)
    assert result == '\x1b[48;5;0m'
    
    # Test with the maximum 8-bit value
    result = eightbit_bg(255)
    assert result == '\x1b[48;5;255m'
