# file: thonny/plugins/pgzero_frontend.py:22-32
# asked: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 32], "branches": []}

import pytest
from unittest.mock import MagicMock

# Mocking the necessary functions and objects
@pytest.fixture
def mock_get_workbench(monkeypatch):
    mock_workbench = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', lambda: mock_workbench)
    return mock_workbench

@pytest.fixture
def mock_tr(monkeypatch):
    mock_translation = MagicMock(return_value="Pygame Zero mode")
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.tr', mock_translation)
    return mock_translation

@pytest.fixture
def mock_update_environment(monkeypatch):
    mock_update = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.update_environment', mock_update)
    return mock_update

@pytest.fixture
def mock_toggle_variable(monkeypatch):
    mock_toggle = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.toggle_variable', mock_toggle)
    return mock_toggle

def test_load_plugin(mock_get_workbench, mock_tr, mock_update_environment, mock_toggle_variable):
    from thonny.plugins.pgzero_frontend import load_plugin, _OPTION_NAME

    # Call the function to test
    load_plugin()

    # Assertions to verify the expected behavior
    mock_get_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
    mock_get_workbench.add_command.assert_called_once_with(
        "toggle_pgzero_mode",
        "run",
        "Pygame Zero mode",
        mock_toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    mock_update_environment.assert_called_once()
