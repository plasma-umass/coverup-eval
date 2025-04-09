# file lib/ansible/plugins/action/include_vars.py:175-189
# lines [180, 181, 182, 183, 184, 185, 186, 187, 189]
# branches ['183->exit', '183->184', '185->186', '185->189']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action.source_dir = "/mock/source/dir"
    action.depth = 2
    return action

@patch("ansible.plugins.action.include_vars.walk")
def test_traverse_dir_depth(mock_walk, action_module):
    # Mock the walk function to return a controlled directory structure
    mock_walk.return_value = [
        ("/mock/source/dir", ["subdir1"], ["file1", "file2"]),
        ("/mock/source/dir/subdir1", [], ["file3", "file4"]),
        ("/mock/source/dir/subdir2", [], ["file5"]),
    ]

    result = list(action_module._traverse_dir_depth())

    # Assertions to verify the correct behavior
    assert result == [
        ("/mock/source/dir", ["file1", "file2"]),
        ("/mock/source/dir/subdir1", ["file3", "file4"]),
    ]

    # Verify that the walk function was called with the correct source directory
    mock_walk.assert_called_once_with("/mock/source/dir")
