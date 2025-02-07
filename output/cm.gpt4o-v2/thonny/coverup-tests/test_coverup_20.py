# file: thonny/plugins/pgzero_frontend.py:15-19
# asked: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}
# gained: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}

import os
import pytest
from unittest.mock import MagicMock
from thonny import get_workbench
from thonny.plugins.pgzero_frontend import update_environment

_OPTION_NAME = "pgzero_mode"

@pytest.fixture
def mock_workbench(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', lambda: mock)
    return mock

def test_update_environment_simple_mode(mock_workbench):
    mock_workbench.in_simple_mode.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    del os.environ["PGZERO_MODE"]

def test_update_environment_not_simple_mode(mock_workbench):
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = "manual"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "manual"
    del os.environ["PGZERO_MODE"]
