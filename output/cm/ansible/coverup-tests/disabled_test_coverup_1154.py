# file lib/ansible/playbook/task.py:410-439
# lines [413, 414, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 436, 437, 439]
# branches ['417->418', '417->429', '419->420', '419->421', '421->422', '421->423', '423->424', '423->425', '430->431', '430->436']

import pytest
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler_task_include import HandlerTaskInclude

@pytest.fixture
def mock_block(mocker):
    mocker.patch('ansible.playbook.block.Block.deserialize')

@pytest.fixture
def mock_role(mocker):
    mocker.patch('ansible.playbook.role.Role.deserialize')

@pytest.fixture
def mock_task_include(mocker):
    mocker.patch('ansible.playbook.task_include.TaskInclude.deserialize')

@pytest.fixture
def mock_handler_task_include(mocker):
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.deserialize')

@pytest.fixture
def task_data():
    return {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'Block',
        'role': {'name': 'test_role'},
        'implicit': True,
        'resolved_action': 'test_action'
    }

def test_deserialize_with_block_parent(task_data, mock_block):
    task = Task()
    task.deserialize(task_data)
    assert isinstance(task._parent, Block)
    assert task.implicit is True
    assert task.resolved_action == 'test_action'

def test_deserialize_with_task_include_parent(task_data, mock_task_include):
    task_data['parent_type'] = 'TaskInclude'
    task = Task()
    task.deserialize(task_data)
    assert isinstance(task._parent, TaskInclude)
    assert task.implicit is True
    assert task.resolved_action == 'test_action'

def test_deserialize_with_handler_task_include_parent(task_data, mock_handler_task_include):
    task_data['parent_type'] = 'HandlerTaskInclude'
    task = Task()
    task.deserialize(task_data)
    assert isinstance(task._parent, HandlerTaskInclude)
    assert task.implicit is True
    assert task.resolved_action == 'test_action'

def test_deserialize_with_role(task_data, mock_role):
    task = Task()
    task.deserialize(task_data)
    assert isinstance(task._role, Role)
    assert task.implicit is True
    assert task.resolved_action == 'test_action'
