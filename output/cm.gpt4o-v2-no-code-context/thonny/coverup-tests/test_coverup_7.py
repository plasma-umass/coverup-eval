# file: thonny/plugins/pgzero_frontend.py:15-19
# asked: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}
# gained: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}

import os
import pytest
from unittest.mock import Mock

# Assuming the function update_environment is imported from thonny.plugins.pgzero_frontend
from thonny.plugins.pgzero_frontend import update_environment, get_workbench, _OPTION_NAME

@pytest.fixture
def mock_workbench(monkeypatch):
    mock = Mock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', lambda: mock)
    return mock

def test_update_environment_simple_mode(mock_workbench):
    mock_workbench.in_simple_mode.return_value = True
    
    update_environment()
    
    assert os.environ["PGZERO_MODE"] == "auto"
    del os.environ["PGZERO_MODE"]

def test_update_environment_advanced_mode(mock_workbench):
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = "some_option_value"
    
    update_environment()
    
    assert os.environ["PGZERO_MODE"] == "some_option_value"
    del os.environ["PGZERO_MODE"]
