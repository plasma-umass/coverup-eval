# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [119, 122], [125, 126], [125, 127], [127, 128], [127, 130]]}
# gained: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [125, 126], [125, 127], [127, 128], [127, 130]]}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task
import ansible.constants as C

class MockTask(Task):
    def get_vars(self):
        return {'mock_var': 'mock_value'}

@pytest.fixture
def mock_task_include(monkeypatch):
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include.vars = {'var1': 'value1'}
    task_include.args = {'arg1': 'value1'}
    task_include._parent = MockTask()
    return task_include

def test_get_vars_include_action(mock_task_include):
    mock_task_include.action = 'include'
    all_vars = mock_task_include.get_vars()
    assert all_vars == {'mock_var': 'mock_value', 'var1': 'value1', 'arg1': 'value1'}

def test_get_vars_non_include_action(mock_task_include, monkeypatch):
    mock_task_include.action = 'non_include'
    def mock_super_get_vars(self):
        return {'super_var': 'super_value'}
    monkeypatch.setattr(Task, 'get_vars', mock_super_get_vars)
    all_vars = mock_task_include.get_vars()
    assert all_vars == {'super_var': 'super_value'}

def test_get_vars_with_tags_and_when(mock_task_include):
    mock_task_include.action = 'include'
    mock_task_include.vars = {'tags': 'sometag', 'when': 'somecondition'}
    all_vars = mock_task_include.get_vars()
    assert 'tags' not in all_vars
    assert 'when' not in all_vars
