# file: lib/ansible/plugins/action/reboot.py:203-209
# asked: {"lines": [204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 204], [205, 206]]}
# gained: {"lines": [204, 205, 206, 207, 208, 209], "branches": [[204, 0], [204, 205], [205, 206]]}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display

@pytest.fixture
def action_module(mocker):
    task = mocker.Mock()
    task.args = {'deprecated_arg': 'value'}
    task.action = 'reboot'
    connection = mocker.Mock()
    play_context = mocker.Mock()
    loader = mocker.Mock()
    templar = mocker.Mock()
    shared_loader_obj = mocker.Mock()
    
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.DEPRECATED_ARGS = {'deprecated_arg': '2.10'}
    return module

def test_deprecated_args_warning(action_module, mocker):
    display = Display()
    mocker.patch('ansible.plugins.action.reboot.display', display)
    mock_warning = mocker.patch.object(display, 'warning')

    action_module.deprecated_args()

    mock_warning.assert_called_once_with('Since Ansible 2.10, deprecated_arg is no longer a valid option for reboot')
