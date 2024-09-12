# file: lib/ansible/playbook/task.py:106-120
# asked: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}
# gained: {"lines": [106, 109, 110, 112, 113, 114, 115, 117, 118, 120], "branches": [[109, 110], [109, 112], [112, 113], [112, 114], [114, 115], [114, 117], [117, 118], [117, 120]]}

import pytest
from ansible.playbook.task import Task

class MockRole:
    def get_name(self, include_role_fqcn=True):
        return "mock_role"

@pytest.fixture
def task_with_role():
    return Task(role=MockRole())

@pytest.fixture
def task_with_name():
    task = Task()
    task.name = "mock_task"
    return task

@pytest.fixture
def task_with_role_and_name():
    task = Task(role=MockRole())
    task.name = "mock_task"
    return task

@pytest.fixture
def task_with_action():
    task = Task()
    task.action = "mock_action"
    return task

def test_get_name_with_role_and_name(task_with_role_and_name):
    assert task_with_role_and_name.get_name() == "mock_role : mock_task"

def test_get_name_with_name(task_with_name):
    assert task_with_name.get_name() == "mock_task"

def test_get_name_with_role(task_with_role):
    task_with_role.action = "mock_action"
    assert task_with_role.get_name() == "mock_role : mock_action"

def test_get_name_with_action(task_with_action):
    assert task_with_action.get_name() == "mock_action"
