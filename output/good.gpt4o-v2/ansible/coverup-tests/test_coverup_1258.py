# file: lib/ansible/playbook/task.py:356-368
# asked: {"lines": [], "branches": [[363, 365], [365, 368]]}
# gained: {"lines": [], "branches": [[363, 365], [365, 368]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.task import Task

@pytest.fixture
def mock_task():
    parent_task = Mock()
    parent_task.get_vars.return_value = {'parent_var': 'value'}
    task = Task(block=None, role=None, task_include=parent_task)
    task.vars = {'task_var': 'value'}
    return task

def test_get_vars_with_tags(mock_task):
    mock_task.vars['tags'] = 'othertag'
    result = mock_task.get_vars()
    assert 'tags' not in result
    assert 'when' not in result
    assert result['parent_var'] == 'value'
    assert result['task_var'] == 'value'

def test_get_vars_with_when(mock_task):
    mock_task.vars['when'] = 'othercondition'
    result = mock_task.get_vars()
    assert 'tags' not in result
    assert 'when' not in result
    assert result['parent_var'] == 'value'
    assert result['task_var'] == 'value'

def test_get_vars_with_tags_and_when(mock_task):
    mock_task.vars['tags'] = 'othertag'
    mock_task.vars['when'] = 'othercondition'
    result = mock_task.get_vars()
    assert 'tags' not in result
    assert 'when' not in result
    assert result['parent_var'] == 'value'
    assert result['task_var'] == 'value'
