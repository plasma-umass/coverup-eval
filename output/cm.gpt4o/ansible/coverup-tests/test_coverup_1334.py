# file lib/ansible/plugins/action/reboot.py:93-95
# lines [95]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming ActionBase is defined somewhere in the ansible.plugins.action.reboot module
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    # Mock the required arguments for ActionModule initialization
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_post_reboot_delay(action_module, mocker):
    # Mock the _check_delay method to ensure it gets called
    mock_check_delay = mocker.patch.object(action_module, '_check_delay', return_value=30)
    
    # Access the post_reboot_delay property to trigger the code
    delay = action_module.post_reboot_delay
    
    # Assert that the _check_delay method was called with the correct parameters
    mock_check_delay.assert_called_once_with('post_reboot_delay', action_module.DEFAULT_POST_REBOOT_DELAY)
    
    # Assert that the returned delay is as expected
    assert delay == 30
