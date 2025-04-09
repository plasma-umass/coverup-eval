# file sty/primitive.py:15-37
# lines [15, 16, 32, 34, 35, 36, 37]
# branches []

import pytest
from sty.primitive import Style, StylingRule

class MockStylingRule:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def test_style_creation():
    # Create mock styling rules
    rule1 = MockStylingRule('\x1b[38;2;1;5;10m')
    rule2 = MockStylingRule('\x1b[1m')

    # Create a Style instance
    style = Style(rule1, rule2, value=str(rule1) + str(rule2))

    # Assertions to verify the correct behavior
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == '\x1b[38;2;1;5;10m\x1b[1m'
    assert style.rules == (rule1, rule2)

    # Clean up
    del style
    del rule1
    del rule2
