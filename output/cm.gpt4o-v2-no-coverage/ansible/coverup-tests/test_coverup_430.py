# file: lib/ansible/playbook/task.py:370-376
# asked: {"lines": [370, 371, 372, 373, 374, 375, 376], "branches": [[372, 373], [372, 374], [374, 375], [374, 376]]}
# gained: {"lines": [370, 371, 372, 373, 374, 375, 376], "branches": [[372, 373], [372, 374], [374, 375], [374, 376]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task import Task
from ansible import constants as C

@pytest.fixture
def mock_task():
    task = Task()
    task._parent = None
    task.action = None
    task.vars = {}
    return task

def test_get_include_params_no_parent_no_action(mock_task):
    result = mock_task.get_include_params()
    assert result == {}

def test_get_include_params_with_parent(mock_task):
    parent_task = MagicMock()
    parent_task.get_include_params.return_value = {'parent_var': 'value'}
    mock_task._parent = parent_task

    result = mock_task.get_include_params()
    assert result == {'parent_var': 'value'}

def test_get_include_params_with_action(mock_task, monkeypatch):
    mock_task.action = 'include'
    mock_task.vars = {'var1': 'value1'}
    
    monkeypatch.setattr(C, '_ACTION_ALL_INCLUDES', ['include'])

    result = mock_task.get_include_params()
    assert result == {'var1': 'value1'}

def test_get_include_params_with_parent_and_action(mock_task, monkeypatch):
    parent_task = MagicMock()
    parent_task.get_include_params.return_value = {'parent_var': 'value'}
    mock_task._parent = parent_task
    mock_task.action = 'include'
    mock_task.vars = {'var1': 'value1'}
    
    monkeypatch.setattr(C, '_ACTION_ALL_INCLUDES', ['include'])

    result = mock_task.get_include_params()
    assert result == {'parent_var': 'value', 'var1': 'value1'}
