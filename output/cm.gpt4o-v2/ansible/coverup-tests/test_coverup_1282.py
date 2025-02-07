# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [], "branches": [[119, 122]]}
# gained: {"lines": [], "branches": [[119, 122]]}

import pytest
from unittest.mock import MagicMock
import ansible.constants as C
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_task_include():
    task_include = TaskInclude()
    task_include._parent = MagicMock()
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value1'}
    return task_include

def test_get_vars_with_parent(mock_task_include):
    mock_task_include._parent.get_vars.return_value = {'parent_var': 'parent_value'}
    mock_task_include.action = 'include'
    
    result = mock_task_include.get_vars()
    
    assert result == {
        'parent_var': 'parent_value',
        'var1': 'value1',
        'arg1': 'value1'
    }

def test_get_vars_without_parent(mock_task_include):
    mock_task_include._parent = None
    mock_task_include.action = 'include'
    
    result = mock_task_include.get_vars()
    
    assert result == {
        'var1': 'value1',
        'arg1': 'value1'
    }
