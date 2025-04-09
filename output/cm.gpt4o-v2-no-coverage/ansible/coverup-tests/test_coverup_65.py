# file: lib/ansible/playbook/task.py:410-439
# asked: {"lines": [410, 413, 414, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 436, 437, 439], "branches": [[417, 418], [417, 429], [419, 420], [419, 421], [421, 422], [421, 423], [423, 424], [423, 425], [430, 431], [430, 436]]}
# gained: {"lines": [410, 413, 414, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 436, 437, 439], "branches": [[417, 418], [417, 429], [419, 420], [419, 421], [421, 422], [421, 423], [423, 424], [430, 431], [430, 436]]}

import pytest
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler_task_include import HandlerTaskInclude

@pytest.fixture
def task_data():
    return {
        'parent': {'some': 'data'},
        'parent_type': 'Block',
        'role': {'role_key': 'role_value'},
        'implicit': True,
        'resolved_action': 'some_action'
    }

@pytest.fixture
def task_instance():
    return Task()

def test_deserialize_with_block_parent(task_instance, task_data, mocker):
    mocker.patch.object(Block, 'deserialize')
    task_instance.deserialize(task_data)
    assert isinstance(task_instance._parent, Block)
    assert task_instance._parent.deserialize.called
    assert task_instance._role is not None
    assert task_instance.implicit is True
    assert task_instance.resolved_action == 'some_action'

def test_deserialize_with_task_include_parent(task_instance, task_data, mocker):
    task_data['parent_type'] = 'TaskInclude'
    mocker.patch.object(TaskInclude, 'deserialize')
    task_instance.deserialize(task_data)
    assert isinstance(task_instance._parent, TaskInclude)
    assert task_instance._parent.deserialize.called

def test_deserialize_with_handler_task_include_parent(task_instance, task_data, mocker):
    task_data['parent_type'] = 'HandlerTaskInclude'
    mocker.patch.object(HandlerTaskInclude, 'deserialize')
    task_instance.deserialize(task_data)
    assert isinstance(task_instance._parent, HandlerTaskInclude)
    assert task_instance._parent.deserialize.called

def test_deserialize_without_parent(task_instance, task_data, mocker):
    task_data.pop('parent')
    mocker.patch.object(Role, 'deserialize')
    task_instance.deserialize(task_data)
    assert task_instance._parent is None
    assert task_instance._role is not None
    assert task_instance._role.deserialize.called

def test_deserialize_without_role(task_instance, task_data, mocker):
    task_data.pop('role')
    task_instance.deserialize(task_data)
    assert task_instance._role is None
    assert task_instance.implicit is True
    assert task_instance.resolved_action == 'some_action'
