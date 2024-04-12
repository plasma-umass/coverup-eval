# file lib/ansible/playbook/task.py:106-120
# lines [109, 110, 112, 113, 114, 115, 117, 118, 120]
# branches ['109->110', '109->112', '112->113', '112->114', '114->115', '114->117', '117->118', '117->120']

import pytest
from ansible.playbook.task import Task

class MockRole:
    def get_name(self, include_role_fqcn=True):
        return "mock_role"

@pytest.fixture
def mock_role(mocker):
    return mocker.Mock(spec=MockRole)

@pytest.fixture
def task_instance(mock_role):
    task = Task()
    task._role = mock_role
    task.name = "test_task"
    task.action = "test_action"
    return task

def test_get_name_with_role_and_name(task_instance, mock_role):
    mock_role.get_name.return_value = "mock_role"
    assert task_instance.get_name() == "mock_role : test_task"

def test_get_name_with_role_and_no_name(task_instance, mock_role):
    task_instance.name = None
    mock_role.get_name.return_value = "mock_role"
    assert task_instance.get_name() == "mock_role : test_action"

def test_get_name_with_no_role_and_name(task_instance):
    task_instance._role = None
    assert task_instance.get_name() == "test_task"

def test_get_name_with_no_role_and_no_name(task_instance):
    task_instance._role = None
    task_instance.name = None
    assert task_instance.get_name() == "test_action"
