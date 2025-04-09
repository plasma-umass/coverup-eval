# file: lib/ansible/playbook/task_include.py:109-130
# asked: {"lines": [109, 115, 116, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 116], [115, 118], [119, 120], [119, 122], [125, 126], [125, 127], [127, 128], [127, 130]]}
# gained: {"lines": [109, 115, 118, 119, 120, 122, 123, 125, 126, 127, 128, 130], "branches": [[115, 118], [119, 120], [119, 122], [125, 126], [125, 127], [127, 128], [127, 130]]}

import pytest
from ansible.playbook.task_include import TaskInclude

class MockTask:
    def get_vars(self):
        return {'mock_var': 'mock_value'}

@pytest.fixture
def task_include():
    return TaskInclude()

def test_get_vars_not_include_action(monkeypatch, task_include):
    monkeypatch.setattr(task_include, 'action', 'some_other_action')
    monkeypatch.setattr(TaskInclude, 'get_vars', MockTask.get_vars)
    result = task_include.get_vars()
    assert result == {'mock_var': 'mock_value'}

def test_get_vars_include_action_no_parent(monkeypatch, task_include):
    monkeypatch.setattr(task_include, 'action', 'include')
    monkeypatch.setattr(task_include, '_parent', None)
    monkeypatch.setattr(task_include, 'vars', {'var1': 'value1'})
    monkeypatch.setattr(task_include, 'args', {'arg1': 'value1'})
    result = task_include.get_vars()
    assert result == {'var1': 'value1', 'arg1': 'value1'}

def test_get_vars_include_action_with_parent(monkeypatch, task_include):
    parent_task = MockTask()
    monkeypatch.setattr(task_include, 'action', 'include')
    monkeypatch.setattr(task_include, '_parent', parent_task)
    monkeypatch.setattr(task_include, 'vars', {'var1': 'value1'})
    monkeypatch.setattr(task_include, 'args', {'arg1': 'value1'})
    result = task_include.get_vars()
    assert result == {'mock_var': 'mock_value', 'var1': 'value1', 'arg1': 'value1'}

def test_get_vars_include_action_with_tags_and_when(monkeypatch, task_include):
    parent_task = MockTask()
    monkeypatch.setattr(task_include, 'action', 'include')
    monkeypatch.setattr(task_include, '_parent', parent_task)
    monkeypatch.setattr(task_include, 'vars', {'var1': 'value1', 'tags': 'sometag', 'when': 'somecondition'})
    monkeypatch.setattr(task_include, 'args', {'arg1': 'value1'})
    result = task_include.get_vars()
    assert result == {'mock_var': 'mock_value', 'var1': 'value1', 'arg1': 'value1'}
    assert 'tags' not in result
    assert 'when' not in result
