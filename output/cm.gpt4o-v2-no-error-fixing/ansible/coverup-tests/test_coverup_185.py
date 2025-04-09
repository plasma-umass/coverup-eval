# file: lib/ansible/plugins/action/include_vars.py:175-189
# asked: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}
# gained: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module.source_dir = "/test/source/dir"
    module.depth = 2
    return module

@patch("ansible.plugins.action.include_vars.walk")
def test_traverse_dir_depth(mock_walk, action_module):
    mock_walk.return_value = [
        ("/test/source/dir", ["subdir1"], ["file1", "file2"]),
        ("/test/source/dir/subdir1", [], ["file3", "file4"]),
        ("/test/source/dir/subdir2", [], ["file5", "file6"]),
    ]

    result = list(action_module._traverse_dir_depth())

    assert result == [
        ("/test/source/dir", ["file1", "file2"]),
        ("/test/source/dir/subdir1", ["file3", "file4"]),
    ]

    mock_walk.assert_called_once_with("/test/source/dir")

@patch("ansible.plugins.action.include_vars.walk")
def test_traverse_dir_depth_unlimited_depth(mock_walk, action_module):
    action_module.depth = 0  # Unlimited depth
    mock_walk.return_value = [
        ("/test/source/dir", ["subdir1"], ["file1", "file2"]),
        ("/test/source/dir/subdir1", [], ["file3", "file4"]),
        ("/test/source/dir/subdir2", [], ["file5", "file6"]),
    ]

    result = list(action_module._traverse_dir_depth())

    assert result == [
        ("/test/source/dir", ["file1", "file2"]),
        ("/test/source/dir/subdir1", ["file3", "file4"]),
        ("/test/source/dir/subdir2", ["file5", "file6"]),
    ]

    mock_walk.assert_called_once_with("/test/source/dir")
