# file sty/primitive.py:142-156
# lines [142, 150, 153, 154, 155, 156]
# branches ['153->exit', '153->154', '155->153', '155->156']

import pytest
from unittest.mock import Mock, patch
from sty.primitive import Register, RenderType, Style

class DummyRenderType(RenderType):
    pass

class DummyStyle(Style):
    pass

@pytest.fixture
def register():
    return Register()

def test_set_renderfunc(register):
    dummy_func = Mock()
    dummy_rendertype = DummyRenderType
    dummy_style = DummyStyle()

    # Mock the renderfuncs attribute
    register.renderfuncs = {}

    # Add an attribute to the register to be an instance of Style
    setattr(register, 'some_style_attr', dummy_style)

    register.set_renderfunc(dummy_rendertype, dummy_func)

    # Assert that the render function was updated in renderfuncs
    assert register.renderfuncs[dummy_rendertype] == dummy_func

    # Assert that the style attribute was updated
    assert getattr(register, 'some_style_attr') == dummy_style
