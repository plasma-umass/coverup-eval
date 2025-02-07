# file: lib/ansible/plugins/action/reboot.py:203-209
# asked: {"lines": [], "branches": [[205, 204]]}
# gained: {"lines": [], "branches": [[205, 204]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def mock_task():
    task = MagicMock()
    task.args = {}
    task.action = 'reboot'
    return task

@pytest.fixture
def action_module(mock_task):
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

@patch('ansible.plugins.action.reboot.display')
def test_deprecated_args_warning(mock_display, action_module, mock_task):
    mock_task.args = {'deprecated_arg': 'value'}
    action_module.DEPRECATED_ARGS = {'deprecated_arg': '2.10'}
    
    action_module.deprecated_args()
    
    mock_display.warning.assert_called_once_with("Since Ansible 2.10, deprecated_arg is no longer a valid option for reboot")

@patch('ansible.plugins.action.reboot.display')
def test_deprecated_args_no_warning(mock_display, action_module, mock_task):
    mock_task.args = {'valid_arg': 'value'}
    action_module.DEPRECATED_ARGS = {'deprecated_arg': '2.10'}
    
    action_module.deprecated_args()
    
    mock_display.warning.assert_not_called()
