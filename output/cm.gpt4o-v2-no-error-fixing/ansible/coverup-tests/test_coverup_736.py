# file: lib/ansible/plugins/action/include_vars.py:153-173
# asked: {"lines": [154, 155, 156, 157, 159, 160, 162, 163, 164, 167, 169, 170, 171, 173], "branches": [[154, 155], [154, 169], [155, 156], [155, 162], [159, 0], [159, 160], [169, 0], [169, 170]]}
# gained: {"lines": [154, 155, 156, 157, 159, 160, 162, 163, 164, 167, 169, 170, 171, 173], "branches": [[154, 155], [154, 169], [155, 156], [155, 162], [159, 160], [169, 170]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    task = Mock()
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_set_root_dir_with_role_and_vars(action_module):
    action_module._task._role = Mock()
    action_module._task._role._role_path = '/role_path'
    action_module.source_dir = 'vars/some_dir'
    
    with patch('os.path.exists', return_value=True):
        action_module._set_root_dir()
    
    assert action_module.source_dir == '/role_path/vars/some_dir'

def test_set_root_dir_with_role_and_non_vars(action_module):
    action_module._task._role = Mock()
    action_module._task._role._role_path = '/role_path'
    action_module.source_dir = 'some_dir'
    
    action_module._set_root_dir()
    
    assert action_module.source_dir == '/role_path/vars/some_dir'

def test_set_root_dir_with_data_source(action_module):
    action_module._task._role = None
    action_module._task._ds = Mock()
    action_module._task._ds._data_source = '/data/source/file.yml'
    action_module.source_dir = 'some_dir'
    
    action_module._set_root_dir()
    
    assert action_module.source_dir == '/data/source/some_dir'
