# file: lib/ansible/playbook/task.py:356-368
# asked: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [363, 365], [365, 366], [365, 368]]}
# gained: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [365, 366]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Task class is imported from ansible.playbook.task
from ansible.playbook.task import Task

@pytest.fixture
def mock_task():
    # Create a mock parent task
    parent_task = MagicMock()
    parent_task.get_vars.return_value = {'parent_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}

    # Create a Task instance with a parent and some vars
    task = Task()
    task._parent = parent_task
    task.vars = {'task_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
    
    return task

def test_get_vars_with_parent(mock_task):
    result = mock_task.get_vars()
    
    # Check that the parent vars are included
    assert 'parent_var' in result
    assert result['parent_var'] == 'value'
    
    # Check that the task vars are included
    assert 'task_var' in result
    assert result['task_var'] == 'value'
    
    # Check that 'tags' and 'when' are removed
    assert 'tags' not in result
    assert 'when' not in result

def test_get_vars_without_parent():
    # Create a Task instance without a parent
    task = Task()
    task._parent = None
    task.vars = {'task_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
    
    result = task.get_vars()
    
    # Check that the task vars are included
    assert 'task_var' in result
    assert result['task_var'] == 'value'
    
    # Check that 'tags' and 'when' are removed
    assert 'tags' not in result
    assert 'when' not in result
