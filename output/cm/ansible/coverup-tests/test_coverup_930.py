# file lib/ansible/plugins/action/reboot.py:86-87
# lines [86, 87]
# branches []

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.loader import action_loader
from unittest.mock import MagicMock

# Mock the Ansible action_loader to return our ActionModule
@pytest.fixture
def action_plugin_mock(mocker):
    mocker.patch.object(action_loader, 'get', return_value=ActionModule)

# Test function to improve coverage
def test_action_module_initialization(action_plugin_mock):
    # Create fake arguments to initialize the ActionModule
    fake_loader = MagicMock()
    fake_task = MagicMock()
    fake_connection = MagicMock()
    fake_play_context = MagicMock()
    fake_loader.get.return_value = MagicMock()
    
    # Initialize the ActionModule
    action_module = ActionModule(fake_task, fake_connection, fake_play_context, fake_loader, MagicMock(), MagicMock())
    
    # Assert that the ActionModule is an instance of ActionBase
    assert isinstance(action_module, ActionModule)
    
    # Clean up after the test
    action_loader.get.reset_mock()
