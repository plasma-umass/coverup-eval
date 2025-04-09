# file: lib/ansible/plugins/action/reboot.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

class MockTask:
    def __init__(self, args):
        self.args = args

@pytest.fixture
def action_module():
    task = MockTask(args={})
    return ActionModule(task, None, None, None, None, None)

def test_pre_reboot_delay_default(action_module, mocker):
    mocker.patch.object(action_module, '_check_delay', return_value=5)
    assert action_module.pre_reboot_delay == 5
    action_module._check_delay.assert_called_once_with('pre_reboot_delay', action_module.DEFAULT_PRE_REBOOT_DELAY)

def test_pre_reboot_delay_custom(action_module, mocker):
    action_module._task.args['pre_reboot_delay'] = 10
    mocker.patch.object(action_module, '_check_delay', return_value=10)
    assert action_module.pre_reboot_delay == 10
    action_module._check_delay.assert_called_once_with('pre_reboot_delay', action_module.DEFAULT_PRE_REBOOT_DELAY)
