# file: sty/primitive.py:132-140
# asked: {"lines": [132, 139, 140], "branches": []}
# gained: {"lines": [132, 139, 140], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    class MockRegister(Register):
        def __init__(self):
            self.renderfuncs = {
                MockRenderType: lambda x, y, z: f"Rendered with {x}, {y}, {z}"
            }
            self.rgb_call = None

    return MockRegister()

def test_set_rgb_call(register):
    register.set_rgb_call(MockRenderType)
    assert register.rgb_call is not None
    assert register.rgb_call(10, 42, 255) == "Rendered with 10, 42, 255"
