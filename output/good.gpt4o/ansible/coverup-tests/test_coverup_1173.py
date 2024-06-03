# file lib/ansible/plugins/action/include_vars.py:249-286
# lines [266, 267, 272]
# branches ['265->266', '271->272', '274->261', '276->261', '278->261', '281->261', '283->261']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule
from ansible.playbook.task import Task

@pytest.fixture
def action_module():
    task = MagicMock(spec=Task)
    task._role = MagicMock()
    task._role._role_path = '/fake/role/path'
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_load_files_in_dir(action_module, mocker):
    root_dir = '/fake/root/dir'
    var_files = ['vars/main.yml', 'valid_file.yml', 'invalid_file.txt']
    
    action_module.files_matching = True
    action_module.matcher = MagicMock()
    action_module.matcher.search.side_effect = lambda x: x != 'invalid_file.txt'
    action_module.ignore_unknown_extensions = True
    action_module._ignore_file = MagicMock(return_value=False)
    action_module._is_valid_file_ext = MagicMock(side_effect=lambda x: x == 'valid_file.yml')
    action_module._load_files = MagicMock(return_value=(False, '', {'key': 'value'}))
    
    with patch('os.path.exists', return_value=True):
        failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)
    
    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}
    action_module.matcher.search.assert_any_call('vars/main.yml')
    action_module.matcher.search.assert_any_call('valid_file.yml')
    action_module.matcher.search.assert_any_call('invalid_file.txt')
    action_module._ignore_file.assert_any_call('valid_file.yml')
    action_module._is_valid_file_ext.assert_any_call('valid_file.yml')
    action_module._load_files.assert_called_once_with('/fake/root/dir/valid_file.yml', validate_extensions=True)
