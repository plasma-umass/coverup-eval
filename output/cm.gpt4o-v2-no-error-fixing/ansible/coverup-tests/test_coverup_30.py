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
        'parent': {'some_key': 'some_value'},
        'parent_type': 'Block',
        'role': {'role_key': 'role_value'},
        'implicit': True,
        'resolved_action': 'some_action',
        'other_data': 'other_value'
    }

def test_deserialize_with_block_parent(task_data):
    task = Task()
    task.deserialize(task_data)
    
    assert isinstance(task._parent, Block)
    assert task._parent._play is None
    assert task.implicit is True
    assert task.resolved_action == 'some_action'
    assert 'parent' not in task_data
    assert 'role' not in task_data

def test_deserialize_with_task_include_parent(task_data, monkeypatch):
    task_data['parent_type'] = 'TaskInclude'
    
    task = Task()
    task.deserialize(task_data)
    
    assert isinstance(task._parent, TaskInclude)
    assert task.implicit is True
    assert task.resolved_action == 'some_action'
    assert 'parent' not in task_data
    assert 'role' not in task_data

def test_deserialize_with_handler_task_include_parent(task_data, monkeypatch):
    task_data['parent_type'] = 'HandlerTaskInclude'
    
    task = Task()
    task.deserialize(task_data)
    
    assert isinstance(task._parent, HandlerTaskInclude)
    assert task.implicit is True
    assert task.resolved_action == 'some_action'
    assert 'parent' not in task_data
    assert 'role' not in task_data

def test_deserialize_with_role(task_data):
    task_data.pop('parent')
    
    task = Task()
    task.deserialize(task_data)
    
    assert isinstance(task._role, Role)
    assert task._role._play is None
    assert task.implicit is True
    assert task.resolved_action == 'some_action'
    assert 'role' not in task_data
