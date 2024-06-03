# file thonny/plugins/pgzero_frontend.py:15-19
# lines [16, 17, 19]
# branches ['16->17', '16->19']

import os
import pytest
from unittest.mock import Mock, patch

# Assuming the function update_environment is imported from thonny.plugins.pgzero_frontend
from thonny.plugins.pgzero_frontend import update_environment

@pytest.fixture
def mock_workbench(mocker):
    mock = mocker.patch('thonny.plugins.pgzero_frontend.get_workbench')
    return mock

def test_update_environment_simple_mode(mock_workbench):
    mock_workbench().in_simple_mode.return_value = True

    update_environment()

    assert os.environ["PGZERO_MODE"] == "auto"

def test_update_environment_advanced_mode(mock_workbench):
    mock_workbench().in_simple_mode.return_value = False
    mock_workbench().get_option.return_value = "advanced"

    update_environment()

    assert os.environ["PGZERO_MODE"] == "advanced"

@pytest.fixture(autouse=True)
def cleanup_environment():
    yield
    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]
