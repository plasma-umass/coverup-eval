# file sty/renderfunc.py:13-14
# lines [13, 14]
# branches []

import pytest
from sty.renderfunc import eightbit_fg

def test_eightbit_fg():
    # Test for a valid color number within the 8-bit range (0-255)
    assert eightbit_fg(42) == "\033[38;5;42m", "The ANSI escape code for foreground color 42 is incorrect"

    # Test for the lower boundary of the 8-bit range
    assert eightbit_fg(0) == "\033[38;5;0m", "The ANSI escape code for foreground color 0 is incorrect"

    # Test for the upper boundary of the 8-bit range
    assert eightbit_fg(255) == "\033[38;5;255m", "The ANSI escape code for foreground color 255 is incorrect"

    # Clean up is not necessary as the function does not alter any state
