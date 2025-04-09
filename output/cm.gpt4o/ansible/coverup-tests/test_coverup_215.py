# file lib/ansible/playbook/task.py:106-120
# lines [106, 109, 110, 112, 113, 114, 115, 117, 118, 120]
# branches ['109->110', '109->112', '112->113', '112->114', '114->115', '114->117', '117->118', '117->120']

import pytest
from unittest.mock import Mock

# Assuming the Task class is imported from ansible.playbook.task
from ansible.playbook.task import Task

@pytest.fixture
def mock_role():
    return Mock()

@pytest.fixture
def task_with_role(mock_role):
    task = Task()
    task._role = mock_role
    task.name = None
    task.action = 'test_action'
    return task

@pytest.fixture
def task_with_name():
    task = Task()
    task._role = None
    task.name = 'test_name'
    task.action = 'test_action'
    return task

@pytest.fixture
def task_with_role_and_name(mock_role):
    task = Task()
    task._role = mock_role
    task.name = 'test_name'
    task.action = 'test_action'
    return task

def test_get_name_with_role_and_name(task_with_role_and_name, mock_role):
    mock_role.get_name.return_value = 'role_name'
    result = task_with_role_and_name.get_name()
    assert result == 'role_name : test_name'

def test_get_name_with_name_only(task_with_name):
    result = task_with_name.get_name()
    assert result == 'test_name'

def test_get_name_with_role_only(task_with_role, mock_role):
    mock_role.get_name.return_value = 'role_name'
    result = task_with_role.get_name()
    assert result == 'role_name : test_action'

def test_get_name_with_action_only():
    task = Task()
    task._role = None
    task.name = None
    task.action = 'test_action'
    result = task.get_name()
    assert result == 'test_action'
