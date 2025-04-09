# file: sty/primitive.py:93-120
# asked: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest
from unittest.mock import MagicMock

from sty.primitive import Register

@pytest.fixture
def register():
    reg = Register()
    reg.is_muted = False
    reg.eightbit_call = MagicMock(return_value="8bit")
    reg.rgb_call = MagicMock(return_value="24bit")
    return reg

def test_register_call_muted(register):
    register.is_muted = True
    assert register() == ""

def test_register_call_eightbit(register):
    assert register(42) == "8bit"
    register.eightbit_call.assert_called_once_with(42)

def test_register_call_rgb(register):
    assert register(102, 49, 42) == "24bit"
    register.rgb_call.assert_called_once_with(102, 49, 42)

def test_register_call_attribute(register):
    setattr(register, 'red', 'red_value')
    assert register('red') == 'red_value'

def test_register_call_invalid(register):
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""
