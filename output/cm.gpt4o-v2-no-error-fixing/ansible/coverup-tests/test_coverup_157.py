# file: lib/ansible/playbook/task_include.py:132-151
# asked: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}
# gained: {"lines": [132, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151], "branches": [[138, 139], [138, 149]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block

class MockParent:
    def __init__(self, play):
        self._play = play

class MockRole:
    pass

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def task_include():
    parent = MockParent(play="mock_play")
    role = MockRole()
    variable_manager = MockVariableManager()
    loader = MockLoader()
    task_include = TaskInclude()
    task_include._parent = parent
    task_include._role = role
    task_include._variable_manager = variable_manager
    task_include._loader = loader
    task_include.args = {'apply': {'some_key': 'some_value'}}
    return task_include

def test_build_parent_block_with_apply(task_include, mocker):
    mocker.patch.object(Block, 'load', return_value="mock_block")
    result = task_include.build_parent_block()
    assert result == "mock_block"
    Block.load.assert_called_once_with(
        {'some_key': 'some_value', 'block': []},
        play="mock_play",
        task_include=task_include,
        role=task_include._role,
        variable_manager=task_include._variable_manager,
        loader=task_include._loader
    )

def test_build_parent_block_without_apply(task_include):
    task_include.args = {}
    result = task_include.build_parent_block()
    assert result == task_include
