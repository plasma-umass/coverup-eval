# file: sty/renderfunc.py:13-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest
from sty.renderfunc import eightbit_fg

def test_eightbit_fg():
    # Test with a sample input
    result = eightbit_fg(42)
    assert result == '\x1b[38;5;42m'
    
    # Test with boundary values
    assert eightbit_fg(0) == '\x1b[38;5;0m'
    assert eightbit_fg(255) == '\x1b[38;5;255m'
