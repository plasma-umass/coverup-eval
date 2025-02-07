# file: lib/ansible/plugins/action/reboot.py:93-95
# asked: {"lines": [93, 94, 95], "branches": []}
# gained: {"lines": [93, 94, 95], "branches": []}

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

def test_post_reboot_delay_default(action_module):
    action_module.DEFAULT_POST_REBOOT_DELAY = 10
    assert action_module.post_reboot_delay == 10

def test_post_reboot_delay_custom(action_module):
    action_module._task.args = {'post_reboot_delay': 5}
    assert action_module.post_reboot_delay == 5

def test_post_reboot_delay_negative(action_module):
    action_module._task.args = {'post_reboot_delay': -5}
    assert action_module.post_reboot_delay == 0
