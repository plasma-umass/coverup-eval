# file: sty/primitive.py:15-37
# asked: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}
# gained: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}

import pytest
from sty.primitive import Style
from typing import Iterable

class MockStylingRule:
    pass

def test_style_creation():
    rule1 = MockStylingRule()
    rule2 = MockStylingRule()
    style = Style(rule1, rule2, value="test")
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == "test"
    assert style.rules == (rule1, rule2)

def test_style_empty_value():
    rule = MockStylingRule()
    style = Style(rule)
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == ""
    assert style.rules == (rule,)
