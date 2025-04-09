# file: lib/ansible/playbook/task.py:394-408
# asked: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [397, 408], [398, 399], [398, 402], [402, 403], [402, 405]]}
# gained: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [398, 399], [398, 402], [402, 403], [402, 405]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def task():
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = None
    task._role = None
    task.implicit = False
    task.resolved_action = 'some_action'
    return task

def test_serialize_no_parent_no_role(task):
    data = task.serialize()
    assert 'parent' not in data
    assert 'parent_type' not in data
    assert 'role' not in data
    assert data['implicit'] == task.implicit
    assert data['resolved_action'] == task.resolved_action

def test_serialize_with_parent(task):
    parent_mock = Mock()
    parent_mock.serialize.return_value = {'key': 'value'}
    parent_mock.__class__.__name__ = 'ParentClass'
    task._parent = parent_mock

    data = task.serialize()
    assert data['parent'] == {'key': 'value'}
    assert data['parent_type'] == 'ParentClass'

def test_serialize_with_role(task):
    role_mock = Mock()
    role_mock.serialize.return_value = {'role_key': 'role_value'}
    task._role = role_mock

    data = task.serialize()
    assert data['role'] == {'role_key': 'role_value'}

def test_serialize_with_parent_and_role(task):
    parent_mock = Mock()
    parent_mock.serialize.return_value = {'key': 'value'}
    parent_mock.__class__.__name__ = 'ParentClass'
    task._parent = parent_mock

    role_mock = Mock()
    role_mock.serialize.return_value = {'role_key': 'role_value'}
    task._role = role_mock

    data = task.serialize()
    assert data['parent'] == {'key': 'value'}
    assert data['parent_type'] == 'ParentClass'
    assert data['role'] == {'role_key': 'role_value'}
    assert data['implicit'] == task.implicit
    assert data['resolved_action'] == task.resolved_action
