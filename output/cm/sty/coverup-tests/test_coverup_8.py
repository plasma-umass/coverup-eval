# file sty/primitive.py:142-156
# lines [142, 150, 153, 154, 155, 156]
# branches ['153->exit', '153->154', '155->153', '155->156']

import pytest
from sty import Register, Style, RenderType
from typing import Callable

class DummyRenderType(RenderType):
    pass

def dummy_render_func():
    pass

@pytest.fixture
def register():
    return Register()

def test_set_renderfunc(register, mocker):
    # Mock the dir function to return a list with a Style attribute
    mocker.patch('sty.primitive.dir', return_value=['dummy_style_attr'])
    # Mock the getattr function to return a Style object when the attribute name is 'dummy_style_attr'
    dummy_style = Style()
    mocker.patch('sty.primitive.getattr', side_effect=lambda x, y: dummy_style if y == 'dummy_style_attr' else None)
    # Mock the setattr function to track calls
    setattr_mock = mocker.patch('sty.primitive.setattr')

    # Call the method to be tested
    register.set_renderfunc(DummyRenderType, dummy_render_func)

    # Check if the render function was updated
    assert register.renderfuncs[DummyRenderType] == dummy_render_func
    # Check if setattr was called with the correct arguments
    setattr_mock.assert_called_once_with(register, 'dummy_style_attr', dummy_style)
