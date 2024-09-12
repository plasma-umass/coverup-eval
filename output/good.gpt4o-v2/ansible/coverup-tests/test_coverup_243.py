# file: lib/ansible/playbook/task_include.py:132-151
# asked: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}
# gained: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block

class MockTask:
    def __init__(self, play=None, role=None, variable_manager=None, loader=None):
        self._play = play
        self._role = role
        self._variable_manager = variable_manager
        self._loader = loader
        self.args = {}

@pytest.fixture
def mock_task():
    return MockTask()

def test_build_parent_block_with_apply(mock_task, monkeypatch):
    task_include = TaskInclude()
    task_include._parent = mock_task
    task_include._role = mock_task._role
    task_include._variable_manager = mock_task._variable_manager
    task_include._loader = mock_task._loader
    task_include.args = {'apply': {'some_key': 'some_value'}}

    def mock_load(data, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
        return Block(play=play, role=role, task_include=task_include)

    monkeypatch.setattr(Block, 'load', mock_load)

    p_block = task_include.build_parent_block()
    assert isinstance(p_block, Block)
    assert p_block._play == mock_task._play
    assert p_block._role == mock_task._role
    assert p_block._parent == task_include

def test_build_parent_block_without_apply(mock_task):
    task_include = TaskInclude()
    task_include._parent = mock_task
    task_include._role = mock_task._role
    task_include._variable_manager = mock_task._variable_manager
    task_include._loader = mock_task._loader
    task_include.args = {}

    p_block = task_include.build_parent_block()
    assert p_block == task_include
