# file: lib/ansible/plugins/action/reboot.py:89-91
# asked: {"lines": [89, 90, 91], "branches": []}
# gained: {"lines": [89, 90, 91], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_pre_reboot_delay_default(action_module):
    assert action_module.pre_reboot_delay == 0

def test_pre_reboot_delay_custom(action_module):
    action_module._task.args['pre_reboot_delay'] = 10
    assert action_module.pre_reboot_delay == 10

def test_pre_reboot_delay_negative(action_module):
    action_module._task.args['pre_reboot_delay'] = -5
    assert action_module.pre_reboot_delay == 0

def test_pre_reboot_delay_sec(action_module):
    action_module._task.args['pre_reboot_delay_sec'] = 15
    assert action_module.pre_reboot_delay == 15
