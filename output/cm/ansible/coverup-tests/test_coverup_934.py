# file lib/ansible/plugins/action/unarchive.py:29-32
# lines [29, 31]
# branches []

import pytest
from ansible.plugins.action.unarchive import ActionModule
from ansible.plugins.loader import action_loader
from ansible.utils.display import Display

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'display')

# Mock the action_loader to prevent actual plugin loading
@pytest.fixture
def mock_action_loader(mocker):
    mocker.patch.object(action_loader, 'get', return_value=ActionModule)

# Test function to check if TRANSFERS_FILES is True
def test_action_module_transfers_files(mock_display, mock_action_loader):
    action_module = ActionModule(None, None, None, None, None, None)
    assert action_module.TRANSFERS_FILES == True
