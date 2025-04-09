# file: sty/primitive.py:40-63
# asked: {"lines": [40, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 61, 63], "branches": [[48, 50], [48, 63], [50, 51], [50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [40, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 61, 63], "branches": [[48, 50], [48, 63], [50, 51], [50, 55], [55, 56], [55, 61]]}

import pytest
from sty.primitive import _render_rules, RenderType, Style, StylingRule

class MockRenderfuncs:
    def __getitem__(self, item):
        return lambda *args: f"rendered_{item.__name__}"

class MockRenderType(RenderType):
    def __init__(self, *args):
        self.args = args

class MockStyle(Style):
    def __init__(self, rules):
        self.rules = rules

def test_render_rules_with_rendertype():
    renderfuncs = MockRenderfuncs()
    rules = [MockRenderType("arg1", "arg2")]
    rendered, flattened_rules = _render_rules(renderfuncs, rules)
    assert rendered == "rendered_MockRenderType"
    assert flattened_rules == rules

def test_render_rules_with_style():
    renderfuncs = MockRenderfuncs()
    nested_rules = [MockRenderType("arg1")]
    rules = [MockStyle(nested_rules)]
    rendered, flattened_rules = _render_rules(renderfuncs, rules)
    assert rendered == "rendered_MockRenderType"
    assert flattened_rules == nested_rules

def test_render_rules_with_invalid_rule():
    renderfuncs = MockRenderfuncs()
    rules = ["invalid_rule"]
    with pytest.raises(ValueError, match=r"Parameter 'rules' must be of type Iterable\[Rule\]."):
        _render_rules(renderfuncs, rules)
