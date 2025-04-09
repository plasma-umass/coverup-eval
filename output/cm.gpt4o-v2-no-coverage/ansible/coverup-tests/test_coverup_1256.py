# file: lib/ansible/plugins/action/include_vars.py:249-286
# asked: {"lines": [258, 259, 260, 261, 262, 264, 265, 266, 267, 269, 270, 271, 272, 274, 275, 276, 277, 278, 279, 281, 282, 283, 284, 286], "branches": [[261, 262], [261, 286], [264, 265], [264, 269], [265, 266], [265, 269], [270, 271], [270, 274], [271, 272], [271, 274], [274, 261], [274, 275], [275, 276], [275, 281], [276, 261], [276, 277], [278, 261], [278, 279], [281, 261], [281, 282], [283, 261], [283, 284]]}
# gained: {"lines": [258, 259, 260, 261, 262, 264, 265, 269, 270, 271, 274, 275, 276, 277, 278, 279, 281, 282, 283, 284, 286], "branches": [[261, 262], [261, 286], [264, 265], [265, 269], [270, 271], [270, 274], [271, 274], [274, 261], [274, 275], [275, 276], [275, 281], [276, 277], [278, 261], [278, 279], [281, 282], [283, 284]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    module = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())
    module._task._role = MagicMock()
    module._task._role._role_path = '/role_path'
    module.files_matching = False
    module.ignore_unknown_extensions = False
    return module

@patch('os.path.exists', return_value=True)
@patch.object(ActionModule, '_ignore_file', return_value=False)
@patch.object(ActionModule, '_is_valid_file_ext', return_value=True)
@patch.object(ActionModule, '_load_files', return_value=(False, '', {'key': 'value'}))
def test_load_files_in_dir(mock_load_files, mock_is_valid_file_ext, mock_ignore_file, mock_path_exists, action_module):
    root_dir = '/root_dir'
    var_files = ['file1.yml', 'file2.yml', 'main.yml']

    action_module._task._role._role_path = '/role_path'
    action_module.files_matching = False
    action_module.ignore_unknown_extensions = True

    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

@patch('os.path.exists', return_value=True)
@patch.object(ActionModule, '_ignore_file', return_value=False)
@patch.object(ActionModule, '_is_valid_file_ext', return_value=True)
@patch.object(ActionModule, '_load_files', return_value=(False, '', {'key': 'value'}))
def test_load_files_in_dir_with_files_matching(mock_load_files, mock_is_valid_file_ext, mock_ignore_file, mock_path_exists, action_module):
    root_dir = '/root_dir'
    var_files = ['file1.yml', 'file2.yml', 'main.yml']

    action_module._task._role._role_path = '/role_path'
    action_module.files_matching = True
    action_module.matcher = MagicMock()
    action_module.matcher.search.return_value = True

    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

@patch('os.path.exists', return_value=True)
@patch.object(ActionModule, '_ignore_file', return_value=False)
@patch.object(ActionModule, '_is_valid_file_ext', return_value=True)
@patch.object(ActionModule, '_load_files', return_value=(True, 'error', {}))
def test_load_files_in_dir_with_failure(mock_load_files, mock_is_valid_file_ext, mock_ignore_file, mock_path_exists, action_module):
    root_dir = '/root_dir'
    var_files = ['file1.yml', 'file2.yml', 'main.yml']

    action_module._task._role._role_path = '/role_path'
    action_module.files_matching = False
    action_module.ignore_unknown_extensions = True

    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    assert failed
    assert err_msg == 'error'
    assert results == {}
