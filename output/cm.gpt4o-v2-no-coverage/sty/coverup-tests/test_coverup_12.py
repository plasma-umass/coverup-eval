# file: sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType
from sty.primitive import Style

def test_set_renderfunc(monkeypatch):
    # Create a mock render function
    def mock_render_func():
        return "rendered"

    # Create a mock RenderType
    class MockRenderType(RenderType):
        pass

    # Create a mock Style
    class MockStyle(Style):
        pass

    # Create an instance of Register
    register = Register()
    register.renderfuncs = {}

    # Add a mock attribute to the register instance
    mock_style = MockStyle()
    setattr(register, 'mock_attr', mock_style)

    # Set the render function
    register.set_renderfunc(MockRenderType, mock_render_func)

    # Assert that the render function was added to renderfuncs
    assert register.renderfuncs[MockRenderType] == mock_render_func

    # Assert that the mock attribute was updated
    assert getattr(register, 'mock_attr') == mock_style

    # Clean up
    del register.renderfuncs
    delattr(register, 'mock_attr')
