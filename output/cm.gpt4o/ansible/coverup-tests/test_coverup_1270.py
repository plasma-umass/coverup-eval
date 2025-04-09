# file lib/ansible/playbook/task.py:394-408
# lines []
# branches ['397->408', '398->402', '402->405']

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def task():
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = Mock()
    task._parent.serialize.return_value = {'key': 'value'}
    task._parent.__class__.__name__ = 'ParentClass'
    task._role = Mock()
    task._role.serialize.return_value = {'role_key': 'role_value'}
    task.implicit = True
    task.resolved_action = 'some_action'
    return task

def test_task_serialize(task):
    data = task.serialize()
    
    assert 'parent' in data
    assert data['parent'] == {'key': 'value'}
    assert 'parent_type' in data
    assert data['parent_type'] == 'ParentClass'
    
    assert 'role' in data
    assert data['role'] == {'role_key': 'role_value'}
    
    assert 'implicit' in data
    assert data['implicit'] is True
    assert 'resolved_action' in data
    assert data['resolved_action'] == 'some_action'

@pytest.fixture
def task_no_parent():
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = None
    task._role = Mock()
    task._role.serialize.return_value = {'role_key': 'role_value'}
    task.implicit = True
    task.resolved_action = 'some_action'
    return task

def test_task_serialize_no_parent(task_no_parent):
    data = task_no_parent.serialize()
    
    assert 'parent' not in data
    assert 'parent_type' not in data
    
    assert 'role' in data
    assert data['role'] == {'role_key': 'role_value'}
    
    assert 'implicit' in data
    assert data['implicit'] is True
    assert 'resolved_action' in data
    assert data['resolved_action'] == 'some_action'

@pytest.fixture
def task_no_role():
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = Mock()
    task._parent.serialize.return_value = {'key': 'value'}
    task._parent.__class__.__name__ = 'ParentClass'
    task._role = None
    task.implicit = True
    task.resolved_action = 'some_action'
    return task

def test_task_serialize_no_role(task_no_role):
    data = task_no_role.serialize()
    
    assert 'parent' in data
    assert data['parent'] == {'key': 'value'}
    assert 'parent_type' in data
    assert data['parent_type'] == 'ParentClass'
    
    assert 'role' not in data
    
    assert 'implicit' in data
    assert data['implicit'] is True
    assert 'resolved_action' in data
    assert data['resolved_action'] == 'some_action'
