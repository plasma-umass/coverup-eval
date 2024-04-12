# file lib/ansible/playbook/task.py:356-368
# lines []
# branches ['358->361', '363->365', '365->368']

import pytest
from ansible.playbook.task import Task

# Mock classes to simulate the necessary behavior
class MockParent:
    def get_vars(self):
        return {'parent_var': 'parent_value', 'tags': 'should_be_deleted', 'when': 'should_be_deleted'}

class MockTask(Task):
    def __init__(self, parent=None):
        self._parent = parent
        self.vars = {'task_var': 'task_value'}

# Test function to cover missing branches
@pytest.fixture
def mock_parent():
    return MockParent()

@pytest.fixture
def task_with_parent(mock_parent):
    return MockTask(parent=mock_parent)

@pytest.fixture
def task_without_parent():
    return MockTask()

def test_task_get_vars_with_parent(task_with_parent):
    vars_with_parent = task_with_parent.get_vars()
    assert 'parent_var' in vars_with_parent
    assert vars_with_parent['parent_var'] == 'parent_value'
    assert 'task_var' in vars_with_parent
    assert vars_with_parent['task_var'] == 'task_value'
    assert 'tags' not in vars_with_parent
    assert 'when' not in vars_with_parent

def test_task_get_vars_without_parent(task_without_parent):
    vars_without_parent = task_without_parent.get_vars()
    assert 'task_var' in vars_without_parent
    assert vars_without_parent['task_var'] == 'task_value'
    assert 'parent_var' not in vars_without_parent
    assert 'tags' not in vars_without_parent
    assert 'when' not in vars_without_parent
