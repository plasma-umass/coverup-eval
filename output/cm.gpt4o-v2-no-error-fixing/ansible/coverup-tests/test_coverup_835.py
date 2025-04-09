# file: lib/ansible/playbook/task.py:394-408
# asked: {"lines": [], "branches": [[397, 408]]}
# gained: {"lines": [], "branches": [[397, 408]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.task import Task

@pytest.fixture
def mock_task():
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = Mock()
    task._parent.serialize.return_value = {'key': 'value'}
    task._parent.__class__.__name__ = 'MockParent'
    task._role = Mock()
    task._role.serialize.return_value = {'role_key': 'role_value'}
    task.implicit = True
    task.resolved_action = 'resolved_action_value'
    return task

def test_serialize_with_parent_and_role(mock_task):
    data = mock_task.serialize()
    assert data['parent'] == {'key': 'value'}
    assert data['parent_type'] == 'MockParent'
    assert data['role'] == {'role_key': 'role_value'}
    assert data['implicit'] is True
    assert data['resolved_action'] == 'resolved_action_value'

def test_serialize_without_parent(mock_task):
    mock_task._parent = None
    data = mock_task.serialize()
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert data['role'] == {'role_key': 'role_value'}
    assert data['implicit'] is True
    assert data['resolved_action'] == 'resolved_action_value'

def test_serialize_without_role(mock_task):
    mock_task._role = None
    data = mock_task.serialize()
    assert data['parent'] == {'key': 'value'}
    assert data['parent_type'] == 'MockParent'
    assert 'role' not in data
    assert data['implicit'] is True
    assert data['resolved_action'] == 'resolved_action_value'

def test_serialize_squashed_or_finalized(mock_task):
    mock_task._squashed = True
    data = mock_task.serialize()
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data
    assert 'implicit' not in data
    assert 'resolved_action' not in data

    mock_task._squashed = False
    mock_task._finalized = True
    data = mock_task.serialize()
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data
    assert 'implicit' not in data
    assert 'resolved_action' not in data
