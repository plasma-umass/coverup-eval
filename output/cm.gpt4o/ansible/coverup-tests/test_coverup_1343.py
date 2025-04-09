# file lib/ansible/plugins/action/reboot.py:89-91
# lines [91]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import PluginLoader
from ansible.template import Templar

@pytest.fixture
def action_module():
    task = MagicMock(spec=Task)
    connection = MagicMock()
    play_context = MagicMock(spec=PlayContext)
    loader = MagicMock(spec=PluginLoader)
    templar = MagicMock(spec=Templar)
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_pre_reboot_delay(action_module, mocker):
    mocker.patch.object(action_module, 'DEFAULT_PRE_REBOOT_DELAY', 5)
    mock_check_delay = mocker.patch.object(action_module, '_check_delay', return_value=10)
    
    result = action_module.pre_reboot_delay
    
    mock_check_delay.assert_called_once_with('pre_reboot_delay', 5)
    assert result == 10
