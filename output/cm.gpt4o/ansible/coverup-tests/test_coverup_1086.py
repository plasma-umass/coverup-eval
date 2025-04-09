# file lib/ansible/playbook/task_include.py:109-130
# lines [115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130]
# branches ['115->116', '115->118', '119->120', '119->122', '125->126', '125->127', '127->128', '127->130']

import pytest
from ansible.playbook.task_include import TaskInclude
from unittest.mock import Mock

@pytest.fixture
def mock_task_include():
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include._parent = Mock()
    task_include._parent.get_vars = Mock(return_value={'parent_var': 'value'})
    task_include.vars = {'var1': 'value1', 'tags': 'sometag'}
    task_include.args = {'arg1': 'value2', 'when': 'somecondition'}
    return task_include

def test_task_include_get_vars(mock_task_include):
    all_vars = mock_task_include.get_vars()
    
    # Assertions to verify the correct behavior
    assert 'parent_var' in all_vars
    assert all_vars['var1'] == 'value1'
    assert all_vars['arg1'] == 'value2'
    assert 'tags' not in all_vars
    assert 'when' not in all_vars

    # Clean up
    mock_task_include._parent.get_vars.reset_mock()
