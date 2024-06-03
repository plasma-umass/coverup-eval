# file lib/ansible/plugins/action/yum.py:29-32
# lines [29, 31]
# branches []

import pytest
from ansible.plugins.action.yum import ActionModule
from ansible.plugins.action import ActionBase
from unittest.mock import Mock

def test_action_module_transfers_files():
    # Ensure the ActionModule class is correctly inheriting from ActionBase
    assert issubclass(ActionModule, ActionBase)
    
    # Mock the required arguments for ActionModule instantiation
    mock_task = Mock()
    mock_connection = Mock()
    mock_play_context = Mock()
    mock_loader = Mock()
    mock_templar = Mock()
    mock_shared_loader_obj = Mock()
    
    # Create an instance of ActionModule with mocked arguments
    action_module_instance = ActionModule(mock_task, mock_connection, mock_play_context, mock_loader, mock_templar, mock_shared_loader_obj)
    
    # Verify that TRANSFERS_FILES is set to False
    assert action_module_instance.TRANSFERS_FILES is False
