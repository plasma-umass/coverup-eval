# file sty/primitive.py:132-140
# lines [132, 139, 140]
# branches []

import pytest
from sty.primitive import Register, RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    reg = Register()
    reg.renderfuncs = {MockRenderType: lambda r, g, b: f"Rendered {r}, {g}, {b}"}
    return reg

def test_set_rgb_call(register):
    register.set_rgb_call(MockRenderType)
    assert register.rgb_call(10, 42, 255) == "Rendered 10, 42, 255"
