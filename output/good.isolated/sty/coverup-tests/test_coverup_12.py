# file sty/primitive.py:142-156
# lines []
# branches ['155->153']

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

def test_set_renderfunc_with_style(register, mocker):
    # Create a dummy Style object and add it as an attribute to the register
    dummy_style = Style()
    setattr(register, 'dummy_style', dummy_style)

    # Call set_renderfunc with the dummy RenderType and render function
    register.set_renderfunc(DummyRenderType, dummy_render_func)

    # Assert that the dummy_style attribute is still present and is a Style object
    assert hasattr(register, 'dummy_style')
    assert isinstance(getattr(register, 'dummy_style'), Style)

    # Clean up by deleting the dummy_style attribute
    delattr(register, 'dummy_style')
