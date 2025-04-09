# file: sty/primitive.py:15-37
# asked: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}
# gained: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}

import pytest
from sty.primitive import Style
from sty.rendertype import RenderType

def test_style_creation_with_rules():
    rule1 = RenderType()  # Assuming RenderType can be instantiated like this
    rule2 = RenderType()
    style = Style(rule1, rule2, value="test_value")
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == "test_value"
    assert style.rules == (rule1, rule2)

def test_style_creation_without_rules():
    style = Style(value="test_value")
    
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == "test_value"
    assert style.rules == ()
