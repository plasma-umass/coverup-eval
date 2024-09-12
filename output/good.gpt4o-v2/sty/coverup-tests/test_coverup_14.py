# file: sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import pytest
from sty.primitive import Register, Style
from sty.rendertype import RenderType

class DummyRenderType(RenderType):
    def __init__(self, *args):
        self.args = args

def dummy_render_func(*args):
    return "dummy_rendered"

def test_register_mute(monkeypatch):
    register = Register()
    
    # Add dummy render functions to the register
    monkeypatch.setitem(register.renderfuncs, DummyRenderType, dummy_render_func)
    
    # Add some Style attributes to the register
    register.style1 = Style(DummyRenderType("rule1"))
    register.style2 = Style(DummyRenderType("rule2"))
    register.non_style_attr = "non-style"

    # Ensure initial state
    assert not register.is_muted
    assert isinstance(register.style1, Style)
    assert isinstance(register.style2, Style)
    assert isinstance(register.non_style_attr, str)

    # Mute the register
    register.mute()

    # Check if the register is muted
    assert register.is_muted

    # Check if Style attributes are still Style instances
    assert isinstance(register.style1, Style)
    assert isinstance(register.style2, Style)
    assert isinstance(register.non_style_attr, str)

    # Clean up
    del register.style1
    del register.style2
    del register.non_style_attr
