# file: sty/primitive.py:93-120
# asked: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest
from sty.primitive import Register

@pytest.fixture
def register():
    return Register()

def test_register_call_muted(register):
    register.is_muted = True
    assert register() == ""

def test_register_call_eightbit(register, mocker):
    mock_eightbit_call = mocker.patch.object(register, 'eightbit_call', return_value="eightbit")
    assert register(42) == "eightbit"
    mock_eightbit_call.assert_called_once_with(42)

def test_register_call_string(register, mocker):
    setattr(register, 'red', "red_value")
    assert register('red') == "red_value"

def test_register_call_rgb(register, mocker):
    mock_rgb_call = mocker.patch.object(register, 'rgb_call', return_value="rgb")
    assert register(102, 49, 42) == "rgb"
    mock_rgb_call.assert_called_once_with(102, 49, 42)

def test_register_call_empty(register):
    assert register(1, 2) == ""
