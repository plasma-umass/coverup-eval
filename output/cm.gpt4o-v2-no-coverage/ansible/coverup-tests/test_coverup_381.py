# file: lib/ansible/plugins/action/include_vars.py:175-189
# asked: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}
# gained: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.include_vars import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

@patch('ansible.plugins.action.include_vars.walk')
def test_traverse_dir_depth_unlimited_depth(mock_walk, action_module):
    action_module.source_dir = '/test/dir'
    action_module.depth = 0  # Unlimited depth

    mock_walk.return_value = [
        ('/test/dir', ('subdir1',), ['file1', 'file2']),
        ('/test/dir/subdir1', (), ['file3', 'file4']),
    ]

    result = list(action_module._traverse_dir_depth())

    assert result == [
        ('/test/dir', ['file1', 'file2']),
        ('/test/dir/subdir1', ['file3', 'file4']),
    ]

@patch('ansible.plugins.action.include_vars.walk')
def test_traverse_dir_depth_limited_depth(mock_walk, action_module):
    action_module.source_dir = '/test/dir'
    action_module.depth = 1  # Limit depth to 1

    mock_walk.return_value = [
        ('/test/dir', ('subdir1',), ['file1', 'file2']),
        ('/test/dir/subdir1', (), ['file3', 'file4']),
    ]

    result = list(action_module._traverse_dir_depth())

    assert result == [
        ('/test/dir', ['file1', 'file2']),
    ]

@patch('ansible.plugins.action.include_vars.walk')
def test_traverse_dir_depth_sorted_files(mock_walk, action_module):
    action_module.source_dir = '/test/dir'
    action_module.depth = 0  # Unlimited depth

    mock_walk.return_value = [
        ('/test/dir', ('subdir1',), ['file2', 'file1']),
        ('/test/dir/subdir1', (), ['file4', 'file3']),
    ]

    result = list(action_module._traverse_dir_depth())

    assert result == [
        ('/test/dir', ['file1', 'file2']),
        ('/test/dir/subdir1', ['file3', 'file4']),
    ]
