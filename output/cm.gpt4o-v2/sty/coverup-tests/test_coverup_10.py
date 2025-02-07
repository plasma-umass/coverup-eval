# file: sty/primitive.py:40-63
# asked: {"lines": [40, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 61, 63], "branches": [[48, 50], [48, 63], [50, 51], [50, 55], [55, 56], [55, 61]]}
# gained: {"lines": [40, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 61, 63], "branches": [[48, 50], [48, 63], [50, 51], [50, 55], [55, 56], [55, 61]]}

import pytest
from sty.primitive import _render_rules
from sty.rendertype import RenderType
from sty import Style

class MockRenderType(RenderType):
    def __init__(self, *args):
        self.args = args

def mock_render_func(*args):
    return "rendered"

def test_render_rules_with_rendertype():
    renderfuncs = {MockRenderType: mock_render_func}
    rules = [MockRenderType(1, 2, 3)]
    rendered, flattened_rules = _render_rules(renderfuncs, rules)
    assert rendered == "rendered"
    assert len(flattened_rules) == 1
    assert isinstance(flattened_rules[0], MockRenderType)

def test_render_rules_with_style():
    renderfuncs = {MockRenderType: mock_render_func}
    nested_rule = MockRenderType(4, 5, 6)
    style_rule = Style(nested_rule, value="styled")
    rules = [style_rule]
    rendered, flattened_rules = _render_rules(renderfuncs, rules)
    assert rendered == "rendered"
    assert len(flattened_rules) == 1
    assert isinstance(flattened_rules[0], MockRenderType)

def test_render_rules_with_invalid_rule():
    renderfuncs = {MockRenderType: mock_render_func}
    rules = ["invalid_rule"]
    with pytest.raises(ValueError, match=r"Parameter 'rules' must be of type Iterable\[Rule\]."):
        _render_rules(renderfuncs, rules)
