# file lib/ansible/playbook/task_include.py:109-130
# lines [115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130]
# branches ['115->116', '115->118', '119->120', '119->122', '125->126', '125->127', '127->128', '127->130']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.utils.sentinel import Sentinel
from unittest.mock import MagicMock

# Assuming C._ACTION_INCLUDE is a constant that needs to be mocked
# and TaskInclude is part of a larger Ansible codebase

@pytest.fixture
def task_include(mocker):
    mocker.patch('ansible.playbook.task_include.C._ACTION_INCLUDE', new=['test_include'])
    task = TaskInclude()
    task.action = 'test_include'
    task.vars = {'var1': 'value1', 'tags': 'should be removed', 'when': 'should be removed'}
    task.args = {'arg1': 'value2'}
    task._parent = MagicMock()
    task._parent.get_vars.return_value = {'parent_var': 'parent_value'}
    return task

def test_task_include_get_vars(task_include):
    # Test the branch where self.action is in C._ACTION_INCLUDE
    all_vars = task_include.get_vars()
    assert 'var1' in all_vars
    assert all_vars['var1'] == 'value1'
    assert 'arg1' in all_vars
    assert all_vars['arg1'] == 'value2'
    assert 'parent_var' in all_vars
    assert all_vars['parent_var'] == 'parent_value'
    assert 'tags' not in all_vars
    assert 'when' not in all_vars

    # Cleanup is handled by pytest fixtures automatically
