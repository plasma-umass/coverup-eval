# file: lib/ansible/plugins/action/reboot.py:116-135
# asked: {"lines": [116, 117, 118, 119, 120, 121, 122, 125, 126, 127, 128, 130, 133, 134, 135], "branches": [[118, 119], [118, 130]]}
# gained: {"lines": [116, 117, 118, 119, 120, 121, 122, 125, 126, 127, 128, 130, 133, 134, 135], "branches": [[118, 119], [118, 130]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common.validation import check_type_str
from ansible.plugins.action.reboot import ActionModule

class MockTask:
    def __init__(self, args):
        self.args = args

@pytest.fixture
def action_module():
    task = MockTask(args={})
    return ActionModule(task, None, None, None, None, None)

def test_get_shutdown_command_args_with_reboot_command(action_module, mocker):
    action_module._task.args = {'reboot_command': 'shutdown -r now'}
    mocker.patch('ansible.plugins.action.reboot.check_type_str', return_value='shutdown -r now')
    result = action_module.get_shutdown_command_args(None)
    assert result == '-r now'

def test_get_shutdown_command_args_with_invalid_reboot_command(action_module, mocker):
    action_module._task.args = {'reboot_command': 12345}
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Invalid type'))
    with pytest.raises(AnsibleError, match="Invalid value given for 'reboot_command'"):
        action_module.get_shutdown_command_args(None)

def test_get_shutdown_command_args_with_empty_reboot_command(action_module, mocker):
    action_module._task.args = {'reboot_command': 'shutdown'}
    mocker.patch('ansible.plugins.action.reboot.check_type_str', return_value='shutdown')
    result = action_module.get_shutdown_command_args(None)
    assert result == ''

def test_get_shutdown_command_args_without_reboot_command(action_module, mocker):
    action_module._task.args = {}
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='{delay_sec} {delay_min} {message}')
    mocker.patch.object(action_module, '_check_delay', return_value=120)
    mocker.patch.object(action_module, 'DEFAULT_REBOOT_MESSAGE', 'Reboot initiated by Ansible')
    result = action_module.get_shutdown_command_args({'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'})
    assert result == '120 2 Reboot initiated by Ansible'
