# file: sty/primitive.py:72-76
# asked: {"lines": [72, 73, 74, 75, 76], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76], "branches": []}

import pytest

from sty.primitive import Register

@pytest.fixture
def register():
    return Register()

def test_register_initial_state(register):
    assert isinstance(register.renderfuncs, dict)
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

def test_eightbit_call(register):
    result = register.eightbit_call(42)
    assert result == 42

def test_rgb_call(register):
    result = register.rgb_call(1, 2, 3)
    assert result == (1, 2, 3)
