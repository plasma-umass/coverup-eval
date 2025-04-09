# file: sty/primitive.py:15-37
# asked: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}
# gained: {"lines": [15, 16, 32, 34, 35, 36, 37], "branches": []}

import pytest
from sty.primitive import Style, StylingRule

class MockStylingRule:
    def __init__(self, rule):
        self.rule = rule

@pytest.fixture
def mock_styling_rule():
    return MockStylingRule("mock_rule")

def test_style_instance(mock_styling_rule):
    style_instance = Style(mock_styling_rule, value="test_value")
    assert isinstance(style_instance, Style)
    assert isinstance(style_instance, str)
    assert style_instance == "test_value"
    assert style_instance.rules == (mock_styling_rule,)

def test_style_multiple_rules(mock_styling_rule):
    another_rule = MockStylingRule("another_rule")
    style_instance = Style(mock_styling_rule, another_rule, value="test_value")
    assert isinstance(style_instance, Style)
    assert isinstance(style_instance, str)
    assert style_instance == "test_value"
    assert style_instance.rules == (mock_styling_rule, another_rule)
