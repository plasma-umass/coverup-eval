# file: sty/primitive.py:122-130
# asked: {"lines": [122, 129, 130], "branches": []}
# gained: {"lines": [122, 129, 130], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    pass

def test_set_eightbit_call():
    register = Register()
    mock_render_func = lambda x: f"Rendered {x}"
    register.renderfuncs[MockRenderType] = mock_render_func

    register.set_eightbit_call(MockRenderType)
    
    assert register.eightbit_call == mock_render_func
    assert register.eightbit_call(144) == "Rendered 144"
