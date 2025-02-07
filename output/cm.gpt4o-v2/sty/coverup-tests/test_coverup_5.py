# file: sty/primitive.py:122-130
# asked: {"lines": [122, 129, 130], "branches": []}
# gained: {"lines": [122, 129, 130], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    pass

def mock_render_function(x):
    return f"Rendered {x}"

@pytest.fixture
def register():
    reg = Register()
    reg.renderfuncs[MockRenderType] = mock_render_function
    return reg

def test_set_eightbit_call(register):
    register.set_eightbit_call(MockRenderType)
    assert register.eightbit_call(144) == "Rendered 144"
