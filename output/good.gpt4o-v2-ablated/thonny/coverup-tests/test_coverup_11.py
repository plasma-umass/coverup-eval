# file: thonny/plugins/pgzero_frontend.py:22-32
# asked: {"lines": [22, 23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}
# gained: {"lines": [22, 23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}

import pytest
from unittest.mock import MagicMock

def test_load_plugin(monkeypatch):
    # Mocking get_workbench and its methods
    mock_workbench = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', lambda: mock_workbench)
    
    # Mocking tr function
    mock_tr = MagicMock(return_value="Pygame Zero mode")
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.tr', mock_tr)
    
    # Mocking update_environment function
    mock_update_environment = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.update_environment', mock_update_environment)
    
    # Mocking toggle_variable
    mock_toggle_variable = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.toggle_variable', mock_toggle_variable)
    
    # Importing the function to test
    from thonny.plugins.pgzero_frontend import load_plugin, _OPTION_NAME
    
    # Call the function
    load_plugin()
    
    # Assertions to verify postconditions
    mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
    mock_workbench.add_command.assert_called_once_with(
        "toggle_pgzero_mode",
        "run",
        "Pygame Zero mode",
        mock_toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    mock_update_environment.assert_called_once()
