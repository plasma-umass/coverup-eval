# file: sty/primitive.py:122-130
# asked: {"lines": [122, 129, 130], "branches": []}
# gained: {"lines": [122, 129, 130], "branches": []}

import pytest
from sty.primitive import Register, RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    return Register()

def test_set_eightbit_call(register, monkeypatch):
    # Mock the renderfuncs dictionary
    mock_renderfuncs = {MockRenderType: lambda x: f"Rendered {x}"}
    monkeypatch.setattr(register, 'renderfuncs', mock_renderfuncs)
    
    # Call the method to be tested
    register.set_eightbit_call(MockRenderType)
    
    # Verify that the eightbit_call attribute is set correctly
    assert register.eightbit_call(144) == "Rendered 144"
