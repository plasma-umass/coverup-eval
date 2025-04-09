# file: lib/ansible/plugins/action/reboot.py:203-209
# asked: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 204], [205, 206]]}
# gained: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 206]]}

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

def test_deprecated_args_no_deprecated_args(action_module, mock_task):
    mock_task.args = {}
    with patch('ansible.plugins.action.reboot.display') as mock_display:
        action_module.deprecated_args()
        mock_display.warning.assert_not_called()

def test_deprecated_args_with_deprecated_args(action_module, mock_task):
    action_module.DEPRECATED_ARGS = {'old_arg': '2.10'}
    mock_task.args = {'old_arg': 'value'}
    with patch('ansible.plugins.action.reboot.display') as mock_display:
        action_module.deprecated_args()
        mock_display.warning.assert_called_once_with("Since Ansible 2.10, old_arg is no longer a valid option for reboot")
