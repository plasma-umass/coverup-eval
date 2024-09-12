# file: sty/primitive.py:122-130
# asked: {"lines": [122, 129, 130], "branches": []}
# gained: {"lines": [122, 129, 130], "branches": []}

import pytest
from sty.primitive import Register, RenderType

class MockRenderType(RenderType):
    pass

@pytest.fixture
def register():
    class MockRegister(Register):
        def __init__(self):
            self.renderfuncs = {
                MockRenderType: lambda x: f"Rendered {x}"
            }
            self.eightbit_call = None

    return MockRegister()

def test_set_eightbit_call(register):
    # Ensure initial state
    assert register.eightbit_call is None

    # Set eightbit call
    register.set_eightbit_call(MockRenderType)

    # Verify the eightbit call is set correctly
    assert register.eightbit_call is not None
    assert register.eightbit_call(144) == "Rendered 144"
