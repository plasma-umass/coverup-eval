# file lib/ansible/playbook/task_include.py:132-151
# lines [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151]
# branches ['138->139', '138->149']

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block

@pytest.fixture
def mock_task_include():
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = MagicMock()
    task_include._parent._play = MagicMock()
    task_include._role = MagicMock()
    task_include._variable_manager = MagicMock()
    task_include._loader = MagicMock()
    return task_include

def test_build_parent_block_with_apply(mock_task_include):
    with patch('ansible.playbook.task_include.Block.load', return_value=MagicMock()) as mock_block_load:
        p_block = mock_task_include.build_parent_block()
        assert 'block' in mock_block_load.call_args[0][0]
        assert isinstance(p_block, MagicMock)
        mock_block_load.assert_called_once_with(
            mock_block_load.call_args[0][0],
            play=mock_task_include._parent._play,
            task_include=mock_task_include,
            role=mock_task_include._role,
            variable_manager=mock_task_include._variable_manager,
            loader=mock_task_include._loader,
        )

def test_build_parent_block_without_apply(mock_task_include):
    mock_task_include.args = {}
    p_block = mock_task_include.build_parent_block()
    assert p_block == mock_task_include
