# file: sty/primitive.py:132-140
# asked: {"lines": [132, 139, 140], "branches": []}
# gained: {"lines": [132, 139, 140], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    pass

def mock_render_func(r, g, b):
    return f"Rendered: {r}, {g}, {b}"

def test_set_rgb_call(monkeypatch):
    register = Register()
    monkeypatch.setattr(register, 'renderfuncs', {MockRenderType: mock_render_func})
    
    register.set_rgb_call(MockRenderType)
    
    assert register.rgb_call(10, 42, 255) == "Rendered: 10, 42, 255"
