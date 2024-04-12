# file thonny/plugins/pgzero_frontend.py:15-19
# lines [15, 16, 17, 19]
# branches ['16->17', '16->19']

import os
import pytest
from thonny.plugins.pgzero_frontend import update_environment
from thonny import get_workbench

# Mocking the get_workbench function
@pytest.fixture
def mock_get_workbench(mocker):
    mock = mocker.Mock()
    mocker.patch('thonny.plugins.pgzero_frontend.get_workbench', return_value=mock)
    return mock

# Test when in simple mode
def test_update_environment_simple_mode(mock_get_workbench):
    mock_get_workbench.in_simple_mode.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    del os.environ["PGZERO_MODE"]  # Clean up

# Test when not in simple mode
def test_update_environment_not_simple_mode(mock_get_workbench):
    mock_get_workbench.in_simple_mode.return_value = False
    _OPTION_NAME = "pgzero_mode"
    expected_option_value = "manual"
    mock_get_workbench.get_option.return_value = expected_option_value
    update_environment()
    assert os.environ["PGZERO_MODE"] == expected_option_value
    del os.environ["PGZERO_MODE"]  # Clean up
