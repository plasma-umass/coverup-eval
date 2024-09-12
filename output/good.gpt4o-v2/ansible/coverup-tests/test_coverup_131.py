# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [119, 122], [125, 126], [125, 127], [127, 128], [127, 130]]}
# gained: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [125, 126], [125, 127], [127, 128], [127, 130]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from unittest.mock import MagicMock, patch

@pytest.fixture
def task_include():
    parent_task = MagicMock()
    parent_task.get_vars.return_value = {'parent_var': 'value'}
    task = TaskInclude()
    task._parent = parent_task
    task.vars = {'var1': 'value1'}
    task.args = {'arg1': 'value2'}
    return task

def test_get_vars_not_include(task_include, monkeypatch):
    monkeypatch.setattr(task_include, 'action', 'some_other_action')
    with patch('ansible.playbook.task.Task.get_vars', return_value={'base_var': 'base_value'}):
        result = task_include.get_vars()
    assert result == {'base_var': 'base_value'}

def test_get_vars_include(task_include, monkeypatch):
    monkeypatch.setattr(task_include, 'action', 'include')
    result = task_include.get_vars()
    assert result == {'parent_var': 'value', 'var1': 'value1', 'arg1': 'value2'}

def test_get_vars_include_with_tags_and_when(task_include, monkeypatch):
    monkeypatch.setattr(task_include, 'action', 'include')
    task_include.vars['tags'] = 'sometag'
    task_include.args['when'] = 'somecondition'
    result = task_include.get_vars()
    assert result == {'parent_var': 'value', 'var1': 'value1', 'arg1': 'value2'}
