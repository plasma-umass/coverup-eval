# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [119, 122], [125, 126], [125, 127], [127, 128], [127, 130]]}
# gained: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [119, 122], [125, 126], [127, 128]]}

import pytest
from unittest.mock import MagicMock
import ansible.constants as C
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def task_include():
    task = TaskInclude()
    task.action = 'include'
    task.vars = {'var1': 'value1', 'tags': 'sometag'}
    task.args = {'arg1': 'value2', 'when': 'somecondition'}
    task._parent = MagicMock()
    task._parent.get_vars = MagicMock(return_value={'parent_var': 'parent_value'})
    return task

def test_get_vars_include_action(task_include):
    task_include.action = 'include'
    all_vars = task_include.get_vars()
    assert all_vars == {'var1': 'value1', 'arg1': 'value2', 'parent_var': 'parent_value'}

def test_get_vars_non_include_action(task_include, monkeypatch):
    task_include.action = 'non_include'
    mock_super_get_vars = MagicMock(return_value={'super_var': 'super_value'})
    monkeypatch.setattr('ansible.playbook.task.Task.get_vars', mock_super_get_vars)
    all_vars = task_include.get_vars()
    mock_super_get_vars.assert_called_once()
    assert all_vars == {'super_var': 'super_value'}

def test_get_vars_include_action_no_parent(task_include):
    task_include.action = 'include'
    task_include._parent = None
    all_vars = task_include.get_vars()
    assert all_vars == {'var1': 'value1', 'arg1': 'value2'}
