# file: sty/primitive.py:132-140
# asked: {"lines": [132, 139, 140], "branches": []}
# gained: {"lines": [132, 139, 140], "branches": []}

import pytest
from sty.primitive import Register, RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    return Register()

def test_set_rgb_call(register, mocker):
    mock_renderfunc = mocker.Mock()
    mocker.patch.object(register, 'renderfuncs', {MockRenderType: mock_renderfunc})
    
    register.set_rgb_call(MockRenderType)
    
    assert register.rgb_call == mock_renderfunc
