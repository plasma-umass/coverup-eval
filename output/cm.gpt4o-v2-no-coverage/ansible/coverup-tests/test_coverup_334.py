# file: lib/ansible/playbook/task_include.py:132-151
# asked: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}
# gained: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block

@pytest.fixture
def task_include():
    parent = MagicMock()
    parent._play = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    role = MagicMock()
    task_include = TaskInclude(
        block=None,
        role=role,
        task_include=None
    )
    task_include._parent = parent
    task_include._variable_manager = variable_manager
    task_include._loader = loader
    task_include._role = role
    return task_include

def test_build_parent_block_with_apply(task_include):
    task_include.args = {'apply': {'some_key': 'some_value'}}
    with patch.object(Block, 'load', return_value='mock_block') as mock_load:
        result = task_include.build_parent_block()
        assert result == 'mock_block'
        mock_load.assert_called_once()
        args, kwargs = mock_load.call_args
        assert 'block' in args[0]
        assert args[0]['block'] == []

def test_build_parent_block_without_apply(task_include):
    task_include.args = {}
    result = task_include.build_parent_block()
    assert result == task_include
