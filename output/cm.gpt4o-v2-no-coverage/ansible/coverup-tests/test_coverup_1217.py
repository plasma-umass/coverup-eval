# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [], "branches": [[119, 122]]}
# gained: {"lines": [], "branches": [[119, 122]]}

import pytest
from unittest.mock import MagicMock, patch
import ansible.constants as C
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def task_include():
    task = TaskInclude()
    task.action = None
    task._parent = None
    task.vars = {}
    task.args = {}
    return task

def test_get_vars_not_include(task_include, mocker):
    mocker.patch('ansible.playbook.task.Task.get_vars', return_value={'key': 'value'})
    task_include.action = 'some_action'
    result = task_include.get_vars()
    assert result == {'key': 'value'}

def test_get_vars_include_no_parent(task_include):
    task_include.action = C._ACTION_INCLUDE[0]
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value2'}
    result = task_include.get_vars()
    assert result == {'var1': 'value1', 'arg1': 'value2'}

def test_get_vars_include_with_parent(task_include, mocker):
    parent_task = MagicMock()
    parent_task.get_vars.return_value = {'parent_var': 'parent_value'}
    task_include._parent = parent_task
    task_include.action = C._ACTION_INCLUDE[0]
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value2'}
    result = task_include.get_vars()
    assert result == {'parent_var': 'parent_value', 'var1': 'value1', 'arg1': 'value2'}

def test_get_vars_include_with_tags_and_when(task_include):
    task_include.action = C._ACTION_INCLUDE[0]
    task_include.vars = {'var1': 'value1', 'tags': 'sometag'}
    task_include.args = {'arg1': 'value2', 'when': 'somecondition'}
    result = task_include.get_vars()
    assert result == {'var1': 'value1', 'arg1': 'value2'}
