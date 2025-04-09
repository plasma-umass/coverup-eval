# file sty/primitive.py:122-130
# lines [122, 129, 130]
# branches []

import pytest
from sty.primitive import Register, RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    return Register()

def test_set_eightbit_call(register, mocker):
    mock_renderfunc = mocker.Mock()
    mock_renderfuncs = {MockRenderType: mock_renderfunc}
    
    # Mock the renderfuncs attribute of the register instance
    mocker.patch.object(register, 'renderfuncs', mock_renderfuncs)
    
    # Call the method to test
    register.set_eightbit_call(MockRenderType)
    
    # Assert that the eightbit_call attribute is set correctly
    assert register.eightbit_call == mock_renderfunc
