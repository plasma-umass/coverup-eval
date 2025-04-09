# file: lib/ansible/playbook/task.py:106-120
# asked: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}
# gained: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

@pytest.fixture
def mock_role():
    role = Mock()
    role.get_name.return_value = "role_name"
    return role

@pytest.fixture
def task_with_role(mock_role):
    return Task(role=mock_role)

@pytest.fixture
def task_without_role():
    return Task()

def test_get_name_with_role_and_name(task_with_role):
    task_with_role.name = "task_name"
    assert task_with_role.get_name() == "role_name : task_name"

def test_get_name_with_name_only(task_without_role):
    task_without_role.name = "task_name"
    assert task_without_role.get_name() == "task_name"

def test_get_name_with_role_only(task_with_role):
    task_with_role.action = "task_action"
    assert task_with_role.get_name() == "role_name : task_action"

def test_get_name_with_action_only(task_without_role):
    task_without_role.action = "task_action"
    assert task_without_role.get_name() == "task_action"
