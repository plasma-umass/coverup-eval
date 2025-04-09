# file lib/ansible/plugins/action/include_vars.py:249-286
# lines [271, 272, 276, 277, 278, 279]
# branches ['264->269', '270->271', '271->272', '271->274', '274->261', '275->276', '276->261', '276->277', '278->261', '278->279', '281->261', '283->261']

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.include_vars import ActionModule

# Define a test function to cover the missing lines and branches
def test_load_files_in_dir(mocker, tmp_path):
    # Setup the test environment
    var_files = ['test1.yml', 'main.yml', 'test2.yml']
    root_dir = str(tmp_path)
    for file in var_files:
        (tmp_path / file).touch()

    # Mock the ActionModule and its dependencies
    action_module = ActionModule(task=mocker.MagicMock(), connection=mocker.MagicMock(), play_context=mocker.MagicMock(), loader=mocker.MagicMock(), templar=mocker.MagicMock(), shared_loader_obj=mocker.MagicMock())
    action_module._task._role = mocker.MagicMock()
    action_module._task._role._role_path = root_dir
    action_module.files_matching = True
    action_module.matcher = mocker.MagicMock()
    action_module.matcher.search.side_effect = lambda x: x == 'test1.yml'
    action_module.ignore_unknown_extensions = True
    action_module._ignore_file = mocker.MagicMock(return_value=False)
    action_module._is_valid_file_ext = mocker.MagicMock(return_value=True)
    action_module._load_files = mocker.MagicMock(return_value=(False, '', {'key': 'value'}))

    # Run the method under test
    failed, err_msg, results = action_module._load_files_in_dir(root_dir, var_files)

    # Assertions to verify the postconditions
    assert not failed
    assert err_msg == ''
    assert results == {'key': 'value'}

    # Verify that the mocked methods were called as expected
    assert action_module.matcher.search.call_count == 3
    action_module.matcher.search.assert_any_call('test1.yml')
    action_module._ignore_file.assert_called()
    action_module._is_valid_file_ext.assert_called()
    action_module._load_files.assert_called()

    # Cleanup after the test
    for file in var_files:
        os.remove(os.path.join(root_dir, file))
