# file lib/ansible/plugins/action/reboot.py:26-75
# lines [26, 27, 28, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 56, 57, 58, 59, 60, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.loader import action_loader

@pytest.fixture
def action_plugin(mocker):
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

@pytest.fixture
def mock_ansible_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.params = {
        'boot_time_command': None,
        'connect_timeout': None,
        'msg': None,
        'post_reboot_delay': None,
        'pre_reboot_delay': None,
        'reboot_command': None,
        'reboot_timeout': None,
        'search_paths': None,
        'test_command': None,
    }
    return mock_module

def test_action_module_default_values(action_plugin, mock_ansible_module, mocker):
    mocker.patch.object(action_loader, 'get', return_value=mock_ansible_module)
    mocker.patch.object(action_plugin, '_execute_module', return_value=dict(changed=True, elapsed=0, rebooted=True))

    result = action_plugin.run(None, None)

    assert 'changed' in result
    assert result['changed'] is True
    assert 'elapsed' in result
    assert result['elapsed'] == 0
    assert 'rebooted' in result
    assert result['rebooted'] is True
