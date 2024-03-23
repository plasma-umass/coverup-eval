# file lib/ansible/playbook/task.py:486-489
# lines [486, 487, 488, 489]
# branches ['487->488', '487->489']

import pytest
from ansible.playbook.task import Task

# Mock class to simulate the parent behavior
class MockParent:
    def all_parents_static(self):
        return False

@pytest.fixture
def mock_parent(mocker):
    mock = mocker.Mock(spec=MockParent)
    mock.all_parents_static.return_value = False
    return mock

@pytest.fixture
def task_with_parent(mock_parent):
    task = Task()
    task._parent = mock_parent
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    return task

def test_all_parents_static_with_parent(task_with_parent):
    assert not task_with_parent.all_parents_static(), "Expected all_parents_static to return False when parent is present and returns False"

def test_all_parents_static_without_parent(task_without_parent):
    assert task_without_parent.all_parents_static(), "Expected all_parents_static to return True when no parent is present"
