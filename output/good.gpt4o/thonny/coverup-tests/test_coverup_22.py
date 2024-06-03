# file thonny/plugins/pgzero_frontend.py:9-12
# lines [10, 11, 12]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the following imports based on the provided code snippet
from thonny.plugins.pgzero_frontend import toggle_variable, _OPTION_NAME
from thonny import get_workbench

@pytest.fixture
def mock_workbench(mocker):
    mock_workbench = mocker.patch('thonny.plugins.pgzero_frontend.get_workbench')
    mock_var = MagicMock()
    mock_var.get.return_value = False
    mock_workbench.return_value.get_variable.return_value = mock_var
    mock_update_environment = mocker.patch('thonny.plugins.pgzero_frontend.update_environment')
    yield mock_workbench, mock_update_environment

def test_toggle_variable(mock_workbench):
    mock_workbench, mock_update_environment = mock_workbench
    toggle_variable()
    
    # Assertions to verify the postconditions
    var = mock_workbench.return_value.get_variable(_OPTION_NAME)
    var.set.assert_called_once_with(True)
    var.get.assert_called_once()
    mock_update_environment.assert_called_once()
