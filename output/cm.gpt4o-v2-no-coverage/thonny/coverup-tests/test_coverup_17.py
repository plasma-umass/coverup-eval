# file: thonny/plugins/pgzero_frontend.py:15-19
# asked: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}
# gained: {"lines": [15, 16, 17, 19], "branches": [[16, 17], [16, 19]]}

import os
import pytest
from thonny import get_workbench
from thonny.plugins.pgzero_frontend import update_environment

_OPTION_NAME = "run.pgzero_mode"

class MockWorkbench:
    def __init__(self, simple_mode, option_value):
        self._simple_mode = simple_mode
        self._option_value = option_value

    def in_simple_mode(self):
        return self._simple_mode

    def get_option(self, option_name):
        assert option_name == _OPTION_NAME
        return self._option_value

@pytest.fixture
def mock_workbench(monkeypatch):
    def mock_get_workbench():
        return MockWorkbench(mock_get_workbench.simple_mode, mock_get_workbench.option_value)
    monkeypatch.setattr('thonny.plugins.pgzero_frontend.get_workbench', mock_get_workbench)
    return mock_get_workbench

def test_update_environment_simple_mode(mock_workbench):
    mock_workbench.simple_mode = True
    mock_workbench.option_value = None  # This value won't be used in simple mode
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'auto'
    del os.environ['PGZERO_MODE']  # Clean up

def test_update_environment_non_simple_mode(mock_workbench):
    mock_workbench.simple_mode = False
    mock_workbench.option_value = 'manual'
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'manual'
    del os.environ['PGZERO_MODE']  # Clean up
