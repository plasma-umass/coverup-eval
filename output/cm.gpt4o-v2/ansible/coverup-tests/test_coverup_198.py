# file: lib/ansible/playbook/task.py:394-408
# asked: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [397, 408], [398, 399], [398, 402], [402, 403], [402, 405]]}
# gained: {"lines": [394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408], "branches": [[397, 398], [398, 399], [398, 402], [402, 403], [402, 405]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def task():
    return Task()

def test_serialize_with_parent(task):
    parent_mock = Mock()
    parent_mock.serialize.return_value = {'key': 'value'}
    parent_mock.__class__.__name__ = 'ParentClass'
    task._parent = parent_mock
    task._squashed = False
    task._finalized = False

    result = task.serialize()

    assert 'parent' in result
    assert result['parent'] == {'key': 'value'}
    assert 'parent_type' in result
    assert result['parent_type'] == 'ParentClass'

def test_serialize_with_role(task):
    role_mock = Mock()
    role_mock.serialize.return_value = {'role_key': 'role_value'}
    task._role = role_mock
    task._squashed = False
    task._finalized = False

    result = task.serialize()

    assert 'role' in result
    assert result['role'] == {'role_key': 'role_value'}

def test_serialize_with_implicit_and_resolved_action(task):
    task.implicit = True
    task.resolved_action = 'some_action'
    task._squashed = False
    task._finalized = False

    result = task.serialize()

    assert 'implicit' in result
    assert result['implicit'] == True
    assert 'resolved_action' in result
    assert result['resolved_action'] == 'some_action'
