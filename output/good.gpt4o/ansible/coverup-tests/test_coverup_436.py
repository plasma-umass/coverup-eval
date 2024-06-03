# file lib/ansible/plugins/action/reboot.py:203-209
# lines [203, 204, 205, 206, 207, 208, 209]
# branches ['204->exit', '204->205', '205->204', '205->206']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.plugins.action.reboot.display.warning')

@pytest.fixture
def action_module():
    task = MagicMock(spec=Task)
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.DEPRECATED_ARGS = {'old_arg': '2.10'}
    return module

def test_deprecated_args_warning(action_module, mock_display_warning):
    action_module._task.args = {'old_arg': 'some_value'}
    action_module._task.action = 'reboot'
    action_module.deprecated_args()
    mock_display_warning.assert_called_once_with("Since Ansible 2.10, old_arg is no longer a valid option for reboot")

def test_deprecated_args_no_warning(action_module, mock_display_warning):
    action_module._task.args = {'new_arg': 'some_value'}
    action_module.deprecated_args()
    mock_display_warning.assert_not_called()
