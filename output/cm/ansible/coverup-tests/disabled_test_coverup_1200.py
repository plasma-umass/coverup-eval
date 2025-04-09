# file lib/ansible/playbook/task.py:394-408
# lines [395, 397, 398, 399, 400, 402, 403, 405, 406, 408]
# branches ['397->398', '397->408', '398->399', '398->402', '402->403', '402->405']

import pytest
from ansible.playbook.task import Task
from ansible.playbook.role import Role
from ansible.playbook.block import Block

@pytest.fixture
def mock_role(mocker):
    role = mocker.MagicMock(spec=Role)
    role.serialize.return_value = {'role_name': 'test_role'}
    return role

@pytest.fixture
def mock_parent(mocker):
    parent = mocker.MagicMock(spec=Block)
    parent.serialize.return_value = {'parent_name': 'test_block'}
    return parent

def test_task_serialize_with_parent_and_role(mock_role, mock_parent):
    task = Task()
    task._squashed = False
    task._finalized = False
    task._parent = mock_parent
    task._role = mock_role
    task.implicit = False
    task.resolved_action = 'test_action'

    serialized_data = task.serialize()

    assert 'parent' in serialized_data
    assert serialized_data['parent'] == {'parent_name': 'test_block'}
    assert 'parent_type' in serialized_data
    assert serialized_data['parent_type'] == 'Block'
    assert 'role' in serialized_data
    assert serialized_data['role'] == {'role_name': 'test_role'}
    assert 'implicit' in serialized_data
    assert serialized_data['implicit'] is False
    assert 'resolved_action' in serialized_data
    assert serialized_data['resolved_action'] == 'test_action'
