# file: lib/ansible/plugins/action/reboot.py:203-209
# asked: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 204], [205, 206]]}
# gained: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 206]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def mock_task():
    task = MagicMock()
    task.args = {'deprecated_arg': 'value'}
    task.action = 'reboot'
    return task

@pytest.fixture
def action_module(mock_task):
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_deprecated_args_warning(action_module, mocker):
    mock_display = mocker.patch('ansible.plugins.action.reboot.display')
    action_module.DEPRECATED_ARGS = {'deprecated_arg': '2.10'}
    
    action_module.deprecated_args()
    
    mock_display.warning.assert_called_once_with("Since Ansible 2.10, deprecated_arg is no longer a valid option for reboot")
