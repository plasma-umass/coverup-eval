# file: thonny/plugins/pgzero_frontend.py:9-12
# asked: {"lines": [9, 10, 11, 12], "branches": []}
# gained: {"lines": [9, 10, 11, 12], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the following functions and variables are defined in the module
# from thonny.plugins.pgzero_frontend import toggle_variable, get_workbench, _OPTION_NAME, update_environment

@pytest.fixture
def mock_get_workbench(monkeypatch):
    mock_workbench = MagicMock()
    mock_var = MagicMock()
    mock_var.get.return_value = False
    mock_workbench.get_variable.return_value = mock_var
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', lambda: mock_workbench)
    return mock_workbench

@pytest.fixture
def mock_update_environment(monkeypatch):
    mock_update = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.update_environment', mock_update)
    return mock_update

def test_toggle_variable(mock_get_workbench, mock_update_environment, monkeypatch):
    from thonny.plugins.pgzero_frontend import toggle_variable, _OPTION_NAME

    toggle_variable()

    var = mock_get_workbench.get_variable(_OPTION_NAME)
    var.set.assert_called_once_with(True)
    mock_update_environment.assert_called_once()
