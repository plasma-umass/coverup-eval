# file lib/ansible/playbook/task.py:378-392
# lines [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392]
# branches ['382->383', '382->385', '386->387', '386->389']

import pytest
from ansible.playbook.task import Task

class MockBase:
    def copy(self):
        return MockBase()

class MockParent(MockBase):
    def copy(self, exclude_tasks=False):
        return MockParent()

class MockRole:
    pass

@pytest.fixture
def mock_task(mocker):
    task = Task()
    task._parent = MockParent()
    task._role = MockRole()
    task.implicit = False
    task.resolved_action = 'some_action'
    return task

def test_task_copy_excluding_parent(mock_task):
    # Test excluding the parent
    new_task = mock_task.copy(exclude_parent=True)
    assert new_task._parent is None
    assert new_task._role is mock_task._role
    assert new_task.implicit == mock_task.implicit
    assert new_task.resolved_action == mock_task.resolved_action

def test_task_copy_including_parent(mock_task):
    # Test including the parent
    new_task = mock_task.copy(exclude_parent=False)
    assert isinstance(new_task._parent, MockParent)
    assert new_task._role is mock_task._role
    assert new_task.implicit == mock_task.implicit
    assert new_task.resolved_action == mock_task.resolved_action

def test_task_copy_excluding_tasks(mock_task):
    # Test excluding tasks in the parent copy
    new_task = mock_task.copy(exclude_parent=False, exclude_tasks=True)
    assert isinstance(new_task._parent, MockParent)
    assert new_task._role is mock_task._role
    assert new_task.implicit == mock_task.implicit
    assert new_task.resolved_action == mock_task.resolved_action
