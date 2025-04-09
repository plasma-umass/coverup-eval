# file: lib/ansible/plugins/action/reboot.py:203-209
# asked: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 204], [205, 206]]}
# gained: {"lines": [203, 204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 204], [205, 206]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    task.action = 'reboot'
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_deprecated_args_no_deprecated(action_module):
    action_module.DEPRECATED_ARGS = {'old_arg': '2.9'}
    action_module._task.args = {'new_arg': 'value'}
    with patch('ansible.plugins.action.reboot.display') as mock_display:
        action_module.deprecated_args()
        mock_display.warning.assert_not_called()

def test_deprecated_args_with_deprecated(action_module):
    action_module.DEPRECATED_ARGS = {'old_arg': '2.9'}
    action_module._task.args = {'old_arg': 'value'}
    with patch('ansible.plugins.action.reboot.display') as mock_display:
        action_module.deprecated_args()
        mock_display.warning.assert_called_once_with(
            "Since Ansible 2.9, old_arg is no longer a valid option for reboot"
        )
