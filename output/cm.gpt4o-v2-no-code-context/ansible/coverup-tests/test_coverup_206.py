# file: lib/ansible/plugins/action/reboot.py:116-135
# asked: {"lines": [116, 117, 118, 119, 120, 121, 122, 125, 126, 127, 128, 130, 133, 134, 135], "branches": [[118, 119], [118, 130]]}
# gained: {"lines": [116, 117, 118, 119, 120, 121, 122, 125, 126, 127, 128, 130, 133, 134, 135], "branches": [[118, 119], [118, 130]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common.validation import check_type_str

class MockTask:
    def __init__(self, args):
        self.args = args

class MockActionModule(ActionModule):
    def __init__(self, task):
        self._task = task
        self._task_vars = {}
        self._templar = None
        self._connection = None
        self._play_context = None
        self._loader = None
        self._shared_loader_obj = None
        self._job_vars = {}
        self._play = None
        self._task_vars = {}
        self._task_vars['pre_reboot_delay'] = 120  # 2 minutes
        self.DEFAULT_REBOOT_MESSAGE = "Rebooting system"

    @property
    def pre_reboot_delay(self):
        return self._task_vars['pre_reboot_delay']

    def _get_value_from_facts(self, *args):
        return "shutdown -r +{delay_min} '{message}'"

@pytest.fixture
def mock_task():
    return MockTask(args={})

@pytest.fixture
def action_module(mock_task):
    return MockActionModule(mock_task)

def test_get_shutdown_command_args_with_reboot_command(action_module):
    action_module._task.args['reboot_command'] = 'shutdown -r now'
    result = action_module.get_shutdown_command_args('any_distribution')
    assert result == '-r now'

def test_get_shutdown_command_args_with_invalid_reboot_command(action_module):
    action_module._task.args['reboot_command'] = 12345
    with pytest.raises(AnsibleError, match="Invalid value given for 'reboot_command'"):
        action_module.get_shutdown_command_args('any_distribution')

def test_get_shutdown_command_args_with_empty_reboot_command(action_module):
    action_module._task.args['reboot_command'] = 'shutdown'
    result = action_module.get_shutdown_command_args('any_distribution')
    assert result == ''

def test_get_shutdown_command_args_without_reboot_command(action_module):
    action_module._task.args.pop('reboot_command', None)
    result = action_module.get_shutdown_command_args('any_distribution')
    assert result == "shutdown -r +2 'Rebooting system'"

def test_get_shutdown_command_args_with_custom_message(action_module):
    action_module._task.args.pop('reboot_command', None)
    action_module._task.args['msg'] = 'Custom reboot message'
    result = action_module.get_shutdown_command_args('any_distribution')
    assert result == "shutdown -r +2 'Custom reboot message'"
