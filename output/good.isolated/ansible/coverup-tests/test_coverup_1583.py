# file lib/ansible/playbook/task_include.py:132-151
# lines [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151]
# branches ['138->139', '138->149']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block
from unittest.mock import MagicMock, patch

# Assuming that the TaskInclude class is part of a larger module that we can import
# and that it has a constructor that we can use to create an instance for testing.

@pytest.fixture
def mock_task_include():
    mock_play = MagicMock()
    mock_role = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    task_include = TaskInclude()
    task_include._parent = MagicMock(_play=mock_play)
    task_include._role = mock_role
    task_include._variable_manager = mock_variable_manager
    task_include._loader = mock_loader
    task_include.args = {'apply': {'tags': 'test'}}
    return task_include

def test_build_parent_block_with_apply(mock_task_include):
    # Mock the Block.load method to avoid validation errors
    with patch.object(Block, 'load', return_value=MagicMock()) as mock_block_load:
        p_block = mock_task_include.build_parent_block()
    
    # Assert that Block.load was called with the expected arguments
    mock_block_load.assert_called_once_with(
        {'block': [], 'tags': 'test'},
        play=mock_task_include._parent._play,
        task_include=mock_task_include,
        role=mock_task_include._role,
        variable_manager=mock_task_include._variable_manager,
        loader=mock_task_include._loader,
    )

    # Clean up by removing the 'apply' attribute to not affect other tests
    mock_task_include.args.pop('apply', None)
