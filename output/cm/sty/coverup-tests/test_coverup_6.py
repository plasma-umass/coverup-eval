# file sty/primitive.py:93-120
# lines [93, 99, 100, 102, 104, 107, 108, 113, 116, 117, 120]
# branches ['99->100', '99->102', '104->107', '104->116', '107->108', '107->113', '116->117', '116->120']

import pytest
from sty.primitive import Register
from unittest.mock import MagicMock

@pytest.fixture
def mock_register():
    register = Register()
    register.is_muted = False
    register.eightbit_call = MagicMock(return_value='eightbit')
    register.rgb_call = MagicMock(return_value='rgb')
    return register

def test_register_call_with_single_int_arg(mock_register):
    assert mock_register(42) == 'eightbit'
    mock_register.eightbit_call.assert_called_once_with(42)

def test_register_call_with_single_str_arg(mock_register):
    setattr(mock_register, 'red', 'color_red')
    assert mock_register('red') == 'color_red'

def test_register_call_with_three_int_args(mock_register):
    assert mock_register(102, 49, 42) == 'rgb'
    mock_register.rgb_call.assert_called_once_with(102, 49, 42)

def test_register_call_with_no_args(mock_register):
    assert mock_register() == ''

def test_register_call_with_muted(mock_register):
    mock_register.is_muted = True
    assert mock_register(42) == ''
    assert mock_register('red') == ''
    assert mock_register(102, 49, 42) == ''
    assert mock_register() == ''
