# file: sty/primitive.py:15-37
# asked: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}
# gained: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}

import pytest
from sty.primitive import Style
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    def __str__(self):
        return "mock_render"

def test_style_creation():
    rule1 = MockRenderType()
    rule2 = MockRenderType()
    style = Style(rule1, rule2, value="test_value")
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == "test_value"
    assert style.rules == (rule1, rule2)

def test_style_empty_value():
    rule = MockRenderType()
    style = Style(rule)
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == ""
    assert style.rules == (rule,)
