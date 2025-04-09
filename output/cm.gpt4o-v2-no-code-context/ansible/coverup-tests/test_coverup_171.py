# file: lib/ansible/playbook/task.py:106-120
# asked: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}
# gained: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}

import pytest
from unittest.mock import Mock

# Assuming the Task class is imported from ansible.playbook.task
from ansible.playbook.task import Task

@pytest.fixture
def mock_role():
    role = Mock()
    role.get_name.return_value = "role_name"
    return role

def test_get_name_with_role_and_name(mock_role):
    task = Task()
    task._role = mock_role
    task.name = "task_name"
    result = task.get_name()
    assert result == "role_name : task_name"

def test_get_name_with_name_only():
    task = Task()
    task._role = None
    task.name = "task_name"
    result = task.get_name()
    assert result == "task_name"

def test_get_name_with_role_only(mock_role):
    task = Task()
    task._role = mock_role
    task.name = None
    task.action = "task_action"
    result = task.get_name()
    assert result == "role_name : task_action"

def test_get_name_with_action_only():
    task = Task()
    task._role = None
    task.name = None
    task.action = "task_action"
    result = task.get_name()
    assert result == "task_action"
