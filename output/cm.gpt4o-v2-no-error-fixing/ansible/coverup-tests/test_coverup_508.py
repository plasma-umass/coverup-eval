# file: lib/ansible/plugins/action/reboot.py:93-95
# asked: {"lines": [93, 94, 95], "branches": []}
# gained: {"lines": [93, 94, 95], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_post_reboot_delay(action_module, mocker):
    mocker.patch.object(action_module, '_check_delay', return_value=10)
    assert action_module.post_reboot_delay == 10
    action_module._check_delay.assert_called_once_with('post_reboot_delay', action_module.DEFAULT_POST_REBOOT_DELAY)
