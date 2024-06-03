# file lib/ansible/plugins/action/include_vars.py:249-286
# lines [266, 267]
# branches ['265->266', '278->261', '281->261', '283->261']

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
    action.ignore_unknown_extensions = True
    return action

@patch('ansible.plugins.action.include_vars.path.exists')
@patch('ansible.plugins.action.include_vars.ActionModule._ignore_file')
@patch('ansible.plugins.action.include_vars.ActionModule._is_valid_file_ext')
@patch('ansible.plugins.action.include_vars.ActionModule._load_files')
def test_load_files_in_dir(mock_load_files, mock_is_valid_file_ext, mock_ignore_file, mock_path_exists, action_module):
    mock_path_exists.side_effect = lambda x: x != '/fake/role/path/vars/main.yml'
    mock_ignore_file.return_value = False
    mock_is_valid_file_ext.return_value = True
    mock_load_files.return_value = (False, '', {'key': 'value'})

    var_files = ['vars/main.yml', 'valid_file.yml']
    failed, err_msg, results = action_module._load_files_in_dir('/fake/role/path', var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}
    assert mock_load_files.call_count == 1
    assert mock_load_files.call_args[0][0] == '/fake/role/path/valid_file.yml'
