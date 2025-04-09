# file lib/ansible/playbook/task_include.py:109-130
# lines [116]
# branches ['115->116', '119->122', '125->127', '127->130']

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

@pytest.fixture
def mock_task_include():
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include._parent = MagicMock()
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value1'}
    return task_include

def test_get_vars_action_not_include(mocker):
    mock_task = TaskInclude()
    mock_task.action = 'not_include'
    mock_super_get_vars = mocker.patch.object(Task, 'get_vars', return_value={'parent_var': 'parent_value'})
    
    result = mock_task.get_vars()
    
    assert result == {'parent_var': 'parent_value'}
    mock_super_get_vars.assert_called_once()

def test_get_vars_with_parent_and_tags(mock_task_include):
    mock_task_include._parent.get_vars.return_value = {'parent_var': 'parent_value', 'tags': 'sometag'}
    
    result = mock_task_include.get_vars()
    
    assert 'tags' not in result
    assert result == {'parent_var': 'parent_value', 'var1': 'value1', 'arg1': 'value1'}

def test_get_vars_with_when(mock_task_include):
    mock_task_include._parent.get_vars.return_value = {'parent_var': 'parent_value', 'when': 'somecondition'}
    
    result = mock_task_include.get_vars()
    
    assert 'when' not in result
    assert result == {'parent_var': 'parent_value', 'var1': 'value1', 'arg1': 'value1'}
