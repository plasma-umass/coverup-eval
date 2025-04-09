# file: lib/ansible/plugins/action/reboot.py:158-201
# asked: {"lines": [158, 159, 160, 161, 162, 163, 164, 165, 167, 169, 170, 172, 173, 175, 177, 178, 179, 180, 182, 183, 184, 185, 187, 188, 190, 191, 192, 193, 194, 198, 199, 200, 201], "branches": [[160, 161], [160, 167], [169, 170], [169, 172], [199, 200], [199, 201]]}
# gained: {"lines": [158, 159, 160, 161, 162, 163, 164, 165, 167, 169, 170, 172, 173, 175, 177, 182, 183, 184, 185, 187, 188, 190, 191, 192, 193, 194, 198, 199, 200, 201], "branches": [[160, 161], [160, 167], [169, 170], [169, 172], [199, 200], [199, 201]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils._text import to_native
from ansible.utils.display import Display

display = Display()

class MockTask:
    def __init__(self, args):
        self.args = args
        self.action = 'reboot'

class MockConnection:
    pass

class MockPlayContext:
    pass

class MockLoader:
    pass

class MockTemplar:
    pass

class MockSharedLoaderObj:
    pass

@pytest.fixture
def action_module():
    task = MockTask(args={})
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_get_shutdown_command_with_reboot_command(action_module, mocker):
    task_vars = {}
    distribution = 'test_distribution'
    action_module._task.args['reboot_command'] = '/sbin/reboot'
    
    mocker.patch('ansible.plugins.action.reboot.check_type_str', return_value='/sbin/reboot')
    
    result = action_module.get_shutdown_command(task_vars, distribution)
    assert result == '/sbin/reboot'

def test_get_shutdown_command_with_invalid_reboot_command(action_module, mocker):
    task_vars = {}
    distribution = 'test_distribution'
    action_module._task.args['reboot_command'] = 12345
    
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Invalid type'))
    
    with pytest.raises(AnsibleError, match="Invalid value given for 'reboot_command'"):
        action_module.get_shutdown_command(task_vars, distribution)

def test_get_shutdown_command_with_default_shutdown_command(action_module, mocker):
    task_vars = {}
    distribution = 'test_distribution'
    
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='shutdown')
    mocker.patch('ansible.plugins.action.reboot.check_type_list', return_value=['/sbin', '/bin'])
    mocker.patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/sbin/shutdown'}]})
    
    result = action_module.get_shutdown_command(task_vars, distribution)
    assert result == '/sbin/shutdown'

def test_get_shutdown_command_with_search_paths(action_module, mocker):
    task_vars = {}
    distribution = 'test_distribution'
    action_module._task.args['search_paths'] = ['/custom/path']
    
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='shutdown')
    mocker.patch('ansible.plugins.action.reboot.check_type_list', return_value=['/custom/path'])
    mocker.patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/custom/path/shutdown'}]})
    
    result = action_module.get_shutdown_command(task_vars, distribution)
    assert result == '/custom/path/shutdown'

def test_get_shutdown_command_with_no_command_found(action_module, mocker):
    task_vars = {}
    distribution = 'test_distribution'
    
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='shutdown')
    mocker.patch('ansible.plugins.action.reboot.check_type_list', return_value=['/sbin', '/bin'])
    mocker.patch.object(action_module, '_execute_module', return_value={'files': []})
    
    with pytest.raises(AnsibleError, match='Unable to find command "shutdown" in search paths'):
        action_module.get_shutdown_command(task_vars, distribution)
