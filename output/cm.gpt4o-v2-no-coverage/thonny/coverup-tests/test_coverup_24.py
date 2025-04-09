# file: thonny/plugins/pgzero_frontend.py:22-32
# asked: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
import os
from thonny.plugins.pgzero_frontend import load_plugin, _OPTION_NAME, toggle_variable, update_environment

@pytest.fixture
def mock_workbench():
    with patch('thonny.plugins.pgzero_frontend.get_workbench') as mock_get_workbench:
        mock_wb = MagicMock()
        mock_get_workbench.return_value = mock_wb
        yield mock_wb

def test_load_plugin(mock_workbench):
    load_plugin()
    mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
    mock_workbench.add_command.assert_called_once_with(
        "toggle_pgzero_mode",
        "run",
        "Pygame Zero mode",
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert 'PGZERO_MODE' in os.environ

def test_toggle_variable(mock_workbench):
    mock_var = MagicMock()
    mock_var.get.return_value = False
    mock_workbench.get_variable.return_value = mock_var

    toggle_variable()

    mock_var.set.assert_called_once_with(True)
    assert 'PGZERO_MODE' in os.environ

@pytest.mark.parametrize("simple_mode, expected_value", [
    (True, 'auto'),
    (False, 'True'),
])
def test_update_environment(mock_workbench, simple_mode, expected_value):
    mock_workbench.in_simple_mode.return_value = simple_mode
    mock_workbench.get_option.return_value = True

    update_environment()

    assert os.environ['PGZERO_MODE'] == expected_value
