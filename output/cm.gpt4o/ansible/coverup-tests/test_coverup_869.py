# file lib/ansible/plugins/action/reboot.py:86-87
# lines [86, 87]
# branches []

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

def test_action_module_init(mocker):
    # Mock the __init__ method of ActionBase to ensure it is called
    mock_init = mocker.patch.object(ActionBase, '__init__', return_value=None)
    
    # Create an instance of ActionModule
    action_module = ActionModule()
    
    # Assert that the ActionBase __init__ method was called
    mock_init.assert_called_once_with()
    
    # Clean up by deleting the instance
    del action_module
