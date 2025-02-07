# file: lib/ansible/plugins/action/include_vars.py:175-189
# asked: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 0], [183, 184], [185, 186], [185, 189]]}
# gained: {"lines": [175, 180, 181, 182, 183, 184, 185, 186, 187, 189], "branches": [[183, 184], [185, 186], [185, 189]]}

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
def test_traverse_dir_depth(mock_walk, action_module):
    # Setup
    action_module.source_dir = '/some/dir'
    action_module.depth = 2
    mock_walk.return_value = [
        ('/some/dir', ('subdir1',), ['file1', 'file2']),
        ('/some/dir/subdir1', (), ['file3', 'file4']),
        ('/some/dir/subdir2', (), ['file5', 'file6'])
    ]

    # Execute
    result = list(action_module._traverse_dir_depth())

    # Verify
    assert result == [
        ('/some/dir', ['file1', 'file2']),
        ('/some/dir/subdir1', ['file3', 'file4']),
    ]

    # Cleanup
    mock_walk.stop()
