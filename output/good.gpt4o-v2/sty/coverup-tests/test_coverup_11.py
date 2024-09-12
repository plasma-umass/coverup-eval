# file: sty/primitive.py:142-156
# asked: {"lines": [142, 150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [142, 150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType
from sty.primitive import Style
from unittest.mock import Mock

class MockRenderType(RenderType):
    pass

def test_set_renderfunc_updates_renderfuncs():
    register = Register()
    mock_func = Mock()
    register.set_renderfunc(MockRenderType, mock_func)
    
    assert register.renderfuncs[MockRenderType] == mock_func

def test_set_renderfunc_updates_style_attributes():
    register = Register()
    mock_func = Mock()
    mock_style = Style()
    
    setattr(register, 'some_style', mock_style)
    setattr(register, 'another_style', mock_style)
    
    register.set_renderfunc(MockRenderType, mock_func)
    
    assert getattr(register, 'some_style') == mock_style
    assert getattr(register, 'another_style') == mock_style
