# file: thonny/plugins/pgzero_frontend.py:9-12
# asked: {"lines": [9, 10, 11, 12], "branches": []}
# gained: {"lines": [9, 10, 11, 12], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
import os

from thonny.plugins.pgzero_frontend import toggle_variable

_OPTION_NAME = "run.pgzero_mode"

@pytest.fixture
def mock_workbench():
    with patch("thonny.plugins.pgzero_frontend.get_workbench") as mock_get_workbench:
        mock_workbench = MagicMock()
        mock_get_workbench.return_value = mock_workbench
        yield mock_workbench

@pytest.fixture
def mock_update_environment():
    with patch("thonny.plugins.pgzero_frontend.update_environment") as mock_update_env:
        yield mock_update_env

def test_toggle_variable(mock_workbench, mock_update_environment):
    # Setup the mock variable
    mock_var = MagicMock()
    mock_var.get.return_value = False
    mock_workbench.get_variable.return_value = mock_var

    # Call the function
    toggle_variable()

    # Assertions
    mock_workbench.get_variable.assert_called_once_with(_OPTION_NAME)
    mock_var.get.assert_called_once()
    mock_var.set.assert_called_once_with(True)
    mock_update_environment.assert_called_once()

    # Cleanup
    if 'PGZERO_MODE' in os.environ:
        del os.environ['PGZERO_MODE']
