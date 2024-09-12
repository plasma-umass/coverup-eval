# file: lib/ansible/playbook/task.py:394-408
# asked: {"lines": [], "branches": [[397, 408]]}
# gained: {"lines": [], "branches": [[397, 408]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def task():
    return Task()

def test_serialize_with_parent_and_role(task):
    # Mocking parent and role
    parent_mock = Mock()
    parent_mock.serialize.return_value = {'parent_key': 'parent_value'}
    parent_mock.__class__.__name__ = 'ParentClass'
    
    role_mock = Mock()
    role_mock.serialize.return_value = {'role_key': 'role_value'}
    
    task._parent = parent_mock
    task._role = role_mock
    task.implicit = True
    task.resolved_action = 'resolved_action_value'
    task._squashed = False
    task._finalized = False
    
    serialized_data = task.serialize()
    
    assert serialized_data['parent'] == {'parent_key': 'parent_value'}
    assert serialized_data['parent_type'] == 'ParentClass'
    assert serialized_data['role'] == {'role_key': 'role_value'}
    assert serialized_data['implicit'] == True
    assert serialized_data['resolved_action'] == 'resolved_action_value'

def test_serialize_without_parent_and_role(task):
    task._parent = None
    task._role = None
    task.implicit = False
    task.resolved_action = 'resolved_action_value'
    task._squashed = False
    task._finalized = False
    
    serialized_data = task.serialize()
    
    assert 'parent' not in serialized_data
    assert 'parent_type' not in serialized_data
    assert 'role' not in serialized_data
    assert serialized_data['implicit'] == False
    assert serialized_data['resolved_action'] == 'resolved_action_value'

def test_serialize_squashed_or_finalized(task):
    task._parent = None
    task._role = None
    task.implicit = False
    task.resolved_action = 'resolved_action_value'
    
    # Case when _squashed is True
    task._squashed = True
    task._finalized = False
    serialized_data = task.serialize()
    assert 'parent' not in serialized_data
    assert 'parent_type' not in serialized_data
    assert 'role' not in serialized_data
    assert 'implicit' not in serialized_data
    assert 'resolved_action' not in serialized_data
    
    # Case when _finalized is True
    task._squashed = False
    task._finalized = True
    serialized_data = task.serialize()
    assert 'parent' not in serialized_data
    assert 'parent_type' not in serialized_data
    assert 'role' not in serialized_data
    assert 'implicit' not in serialized_data
    assert 'resolved_action' not in serialized_data
