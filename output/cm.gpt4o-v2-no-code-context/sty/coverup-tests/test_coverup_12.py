# file: sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

import pytest
from sty.primitive import Register, RenderType, Style

class MockRenderType(RenderType):
    pass

class MockStyle(Style):
    pass

@pytest.fixture
def register():
    reg = Register()
    reg.mock_style_attr = MockStyle()  # Manually add a mock style attribute
    return reg

def test_set_renderfunc_updates_renderfuncs(register):
    def mock_func():
        pass

    register.set_renderfunc(MockRenderType, mock_func)
    assert register.renderfuncs[MockRenderType] == mock_func

def test_set_renderfunc_updates_styles(register):
    def mock_func():
        pass

    original_style = register.mock_style_attr

    register.set_renderfunc(MockRenderType, mock_func)
    assert getattr(register, 'mock_style_attr') == original_style
