# file: sty/primitive.py:132-140
# asked: {"lines": [132, 139, 140], "branches": []}
# gained: {"lines": [132, 139, 140], "branches": []}

import pytest
from sty.primitive import Register
from sty.rendertype import RenderType

class MockRenderType(RenderType):
    pass

def mock_render_func():
    return "mocked"

@pytest.fixture
def register():
    return Register()

def test_set_rgb_call(register, monkeypatch):
    # Mock the renderfuncs dictionary
    monkeypatch.setattr(register, 'renderfuncs', {MockRenderType: mock_render_func})
    
    # Call set_rgb_call with the mock render type
    register.set_rgb_call(MockRenderType)
    
    # Assert that the rgb_call is set to the mock render function
    assert register.rgb_call == mock_render_func
