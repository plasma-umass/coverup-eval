# file: lib/ansible/playbook/task.py:394-408
# asked: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [397, 408], [398, 399], [398, 402], [402, 403], [402, 405]]}
# gained: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [397, 408], [398, 399], [398, 402], [402, 403], [402, 405]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def task():
    return Task()

def test_serialize_no_squash_no_finalize_no_parent_no_role(task):
    task._squashed = False
    task._finalized = False
    task._parent = None
    task._role = None
    task.implicit = True
    task.resolved_action = 'action'
    
    data = task.serialize()
    
    assert data['implicit'] == True
    assert data['resolved_action'] == 'action'
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data

def test_serialize_with_parent(task):
    parent_task = Mock()
    parent_task.serialize.return_value = {'key': 'value'}
    parent_task.__class__.__name__ = 'ParentTask'
    
    task._squashed = False
    task._finalized = False
    task._parent = parent_task
    task._role = None
    task.implicit = True
    task.resolved_action = 'action'
    
    data = task.serialize()
    
    assert data['parent'] == {'key': 'value'}
    assert data['parent_type'] == 'ParentTask'
    assert data['implicit'] == True
    assert data['resolved_action'] == 'action'
    assert 'role' not in data

def test_serialize_with_role(task):
    role = Mock()
    role.serialize.return_value = {'role_key': 'role_value'}
    
    task._squashed = False
    task._finalized = False
    task._parent = None
    task._role = role
    task.implicit = True
    task.resolved_action = 'action'
    
    data = task.serialize()
    
    assert data['role'] == {'role_key': 'role_value'}
    assert data['implicit'] == True
    assert data['resolved_action'] == 'action'
    assert 'parent' not in data
    assert 'parent_type' not in data

def test_serialize_squashed(task):
    task._squashed = True
    task._finalized = False
    task._parent = None
    task._role = None
    task.implicit = True
    task.resolved_action = 'action'
    
    data = task.serialize()
    
    assert 'implicit' not in data
    assert 'resolved_action' not in data
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data

def test_serialize_finalized(task):
    task._squashed = False
    task._finalized = True
    task._parent = None
    task._role = None
    task.implicit = True
    task.resolved_action = 'action'
    
    data = task.serialize()
    
    assert 'implicit' not in data
    assert 'resolved_action' not in data
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data
