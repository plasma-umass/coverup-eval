# file lib/ansible/playbook/task.py:410-439
# lines [410, 413, 414, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 436, 437, 439]
# branches ['417->418', '417->429', '419->420', '419->421', '421->422', '421->423', '423->424', '423->425', '430->431', '430->436']

import pytest
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler_task_include import HandlerTaskInclude

@pytest.fixture
def mock_block(mocker):
    mock = mocker.MagicMock(spec=Block)
    mock.deserialize = mocker.MagicMock()
    return mock

@pytest.fixture
def mock_task_include(mocker):
    mock = mocker.MagicMock(spec=TaskInclude)
    mock.deserialize = mocker.MagicMock()
    return mock

@pytest.fixture
def mock_handler_task_include(mocker):
    mock = mocker.MagicMock(spec=HandlerTaskInclude)
    mock.deserialize = mocker.MagicMock()
    return mock

@pytest.fixture
def mock_role(mocker):
    mock = mocker.MagicMock(spec=Role)
    mock.deserialize = mocker.MagicMock()
    return mock

@pytest.fixture
def task_class(mocker, mock_block, mock_task_include, mock_handler_task_include, mock_role):
    mocker.patch.object(Block, '__new__', return_value=mock_block)
    mocker.patch.object(TaskInclude, '__new__', return_value=mock_task_include)
    mocker.patch.object(HandlerTaskInclude, '__new__', return_value=mock_handler_task_include)
    mocker.patch.object(Role, '__new__', return_value=mock_role)
    return Task

def test_task_deserialize_with_parent_block(task_class):
    data = {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'Block',
        'role': {'name': 'test_role'}
    }
    task = task_class()
    task.deserialize(data)

    assert isinstance(task._parent, Block)
    assert 'parent' not in data
    assert isinstance(task._role, Role)
    assert 'role' not in data

def test_task_deserialize_with_parent_task_include(task_class):
    data = {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'TaskInclude',
        'role': {'name': 'test_role'}
    }
    task = task_class()
    task.deserialize(data)

    assert isinstance(task._parent, TaskInclude)
    assert 'parent' not in data
    assert isinstance(task._role, Role)
    assert 'role' not in data

def test_task_deserialize_with_parent_handler_task_include(task_class):
    data = {
        'parent': {'dummy_key': 'dummy_value'},
        'parent_type': 'HandlerTaskInclude',
        'role': {'name': 'test_role'}
    }
    task = task_class()
    task.deserialize(data)

    assert isinstance(task._parent, HandlerTaskInclude)
    assert 'parent' not in data
    assert isinstance(task._role, Role)
    assert 'role' not in data
