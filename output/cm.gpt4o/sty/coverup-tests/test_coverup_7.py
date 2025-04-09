# file sty/primitive.py:93-120
# lines [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120]
# branches ['99->100', '99->102', '104->107', '104->116', '107->108', '107->113', '116->117', '116->120']

import pytest
from unittest.mock import MagicMock
from sty.primitive import Register

@pytest.fixture
def register():
    reg = Register()
    reg.is_muted = False
    reg.eightbit_call = MagicMock(return_value="8bit_color")
    reg.rgb_call = MagicMock(return_value="24bit_color")
    reg.red = "red_color"
    return reg

def test_register_eightbit_call(register):
    result = register(42)
    register.eightbit_call.assert_called_once_with(42)
    assert result == "8bit_color"

def test_register_rgb_call(register):
    result = register(102, 49, 42)
    register.rgb_call.assert_called_once_with(102, 49, 42)
    assert result == "24bit_color"

def test_register_string_attribute(register):
    result = register("red")
    assert result == "red_color"

def test_register_no_args(register):
    result = register()
    assert result == ""

def test_register_invalid_args(register):
    result = register(1, 2)
    assert result == ""

def test_register_muted(register):
    register.is_muted = True
    result = register(42)
    assert result == ""
