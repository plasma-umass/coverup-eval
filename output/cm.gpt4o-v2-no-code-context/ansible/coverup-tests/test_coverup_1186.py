# file: lib/ansible/plugins/action/include_vars.py:249-286
# asked: {"lines": [], "branches": [[264, 269], [278, 261], [281, 261], [283, 261]]}
# gained: {"lines": [], "branches": [[281, 261]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule
from os import path

@pytest.fixture
def action_module():
    task = MagicMock()
    task._role = MagicMock()
    task._role._role_path = '/fake/role/path'
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    action = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    action._task = task
    action.files_matching = False
    action.matcher = MagicMock()
    action.ignore_unknown_extensions = False
    return action

def test_load_files_in_dir_with_role_main_yml(action_module):
    var_files = ['vars/main.yml', 'other.yml']
    root_dir = '/fake/role/path'
    action_module._task._role = MagicMock()
    action_module._task._role._role_path = '/fake/role/path'
    
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)
    
    assert not failed
    assert err_msg == ''
    assert results == {}

def test_load_files_in_dir_with_files_matching(action_module):
    var_files = ['file1.yml', 'file2.yml']
    root_dir = '/fake/dir'
    action_module.files_matching = True
    action_module.matcher.search = MagicMock(return_value=False)
    
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)
    
    assert not failed
    assert err_msg == ''
    assert results == {}

def test_load_files_in_dir_ignore_unknown_extensions(action_module):
    var_files = ['file1.yml']
    root_dir = '/fake/dir'
    action_module.ignore_unknown_extensions = True
    action_module._ignore_file = MagicMock(return_value=False)
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._load_files = MagicMock(return_value=(False, '', {'key': 'value'}))
    
    with patch('os.path.exists', return_value=True):
        failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)
    
    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

def test_load_files_in_dir_no_ignore_unknown_extensions(action_module):
    var_files = ['file1.yml']
    root_dir = '/fake/dir'
    action_module.ignore_unknown_extensions = False
    action_module._ignore_file = MagicMock(return_value=False)
    action_module._load_files = MagicMock(return_value=(False, '', {'key': 'value'}))
    
    with patch('os.path.exists', return_value=True):
        failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)
    
    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}
