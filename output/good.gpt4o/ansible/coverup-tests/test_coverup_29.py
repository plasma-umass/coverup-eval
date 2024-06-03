# file lib/ansible/plugins/action/include_vars.py:249-286
# lines [249, 258, 259, 260, 261, 262, 264, 265, 266, 267, 269, 270, 271, 272, 274, 275, 276, 277, 278, 279, 281, 282, 283, 284, 286]
# branches ['261->262', '261->286', '264->265', '264->269', '265->266', '265->269', '270->271', '270->274', '271->272', '271->274', '274->261', '274->275', '275->276', '275->281', '276->261', '276->277', '278->261', '278->279', '281->261', '281->282', '283->261', '283->284']

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
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    action_module.files_matching = False
    action_module.matcher = MagicMock()
    action_module.ignore_unknown_extensions = False
    action_module._ignore_file = MagicMock(return_value=False)
    action_module._is_valid_file_ext = MagicMock(return_value=True)
    action_module._load_files = MagicMock(return_value=(False, '', {'key': 'value'}))
    return action_module

@patch('os.path.exists', return_value=True)
def test_load_files_in_dir(mock_exists, action_module):
    root_dir = '/fake/root/dir'
    var_files = ['vars/main.yml', 'vars/other.yml']

    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

    action_module._task._role = None
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

    action_module.files_matching = True
    action_module.matcher.search = MagicMock(return_value=True)
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

    action_module.ignore_unknown_extensions = True
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}
