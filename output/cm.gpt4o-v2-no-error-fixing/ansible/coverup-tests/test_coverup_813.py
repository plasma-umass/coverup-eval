# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [], "branches": [[125, 127], [127, 130]]}
# gained: {"lines": [], "branches": [[125, 127], [127, 130]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from unittest.mock import MagicMock

@pytest.fixture
def task_include():
    task = TaskInclude()
    task.action = 'include'
    task._parent = MagicMock()
    task.vars = {'var1': 'value1', 'tags': 'sometag'}
    task.args = {'arg1': 'value2', 'when': 'somecondition'}
    return task

def test_get_vars_with_tags_and_when(task_include):
    all_vars = task_include.get_vars()
    assert 'tags' not in all_vars
    assert 'when' not in all_vars
    assert all_vars['var1'] == 'value1'
    assert all_vars['arg1'] == 'value2'

def test_get_vars_without_tags_and_when(task_include):
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value2'}
    all_vars = task_include.get_vars()
    assert 'tags' not in all_vars
    assert 'when' not in all_vars
    assert all_vars['var1'] == 'value1'
    assert all_vars['arg1'] == 'value2'
