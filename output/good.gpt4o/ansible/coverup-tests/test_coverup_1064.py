# file lib/ansible/plugins/action/reboot.py:158-201
# lines [159, 160, 161, 162, 163, 164, 165, 167, 169, 170, 172, 173, 175, 177, 178, 179, 180, 182, 183, 184, 185, 187, 188, 190, 191, 192, 193, 194, 198, 199, 200, 201]
# branches ['160->161', '160->167', '169->170', '169->172', '199->200', '199->201']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common.validation import check_type_str, check_type_list
from unittest.mock import patch, MagicMock

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

def test_get_shutdown_command_with_reboot_command(action_module, mocker):
    action_module._task.args['reboot_command'] = 'reboot now'
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=check_type_str)
    mocker.patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/sbin/reboot'}]})
    
    result = action_module.get_shutdown_command({}, 'any_distribution')
    assert result == '/sbin/reboot'

def test_get_shutdown_command_with_invalid_reboot_command(action_module, mocker):
    action_module._task.args['reboot_command'] = 12345
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Invalid type'))
    
    with pytest.raises(AnsibleError, match="Invalid value given for 'reboot_command'"):
        action_module.get_shutdown_command({}, 'any_distribution')

def test_get_shutdown_command_with_default_search_paths(action_module, mocker):
    action_module._task.args['reboot_command'] = 'reboot'
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=check_type_str)
    mocker.patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/sbin/reboot'}]})
    
    result = action_module.get_shutdown_command({}, 'any_distribution')
    assert result == '/sbin/reboot'

def test_get_shutdown_command_with_custom_search_paths(action_module, mocker):
    action_module._task.args['reboot_command'] = 'reboot'
    action_module._task.args['search_paths'] = ['/custom/path']
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=check_type_str)
    mocker.patch('ansible.plugins.action.reboot.check_type_list', side_effect=check_type_list)
    mocker.patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/custom/path/reboot'}]})
    
    result = action_module.get_shutdown_command({}, 'any_distribution')
    assert result == '/custom/path/reboot'

def test_get_shutdown_command_with_invalid_search_paths(action_module, mocker):
    action_module._task.args['reboot_command'] = 'reboot'
    action_module._task.args['search_paths'] = 12345
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=check_type_str)
    mocker.patch('ansible.plugins.action.reboot.check_type_list', side_effect=TypeError)
    
    with pytest.raises(AnsibleError, match="'search_paths' must be a string or flat list of strings"):
        action_module.get_shutdown_command({}, 'any_distribution')

def test_get_shutdown_command_command_not_found(action_module, mocker):
    action_module._task.args['reboot_command'] = 'reboot'
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=check_type_str)
    mocker.patch.object(action_module, '_execute_module', return_value={'files': []})
    
    with pytest.raises(AnsibleError, match='Unable to find command "reboot" in search paths'):
        action_module.get_shutdown_command({}, 'any_distribution')
