# file: lib/ansible/playbook/task.py:141-146
# asked: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}
# gained: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task import Task
from ansible import constants as C

@pytest.fixture
def task():
    task = Task()
    task.args = {'_raw_params': 'test_params'}
    return task

def test_task_repr_meta(task, monkeypatch):
    monkeypatch.setattr(task, 'get_name', lambda: 'meta')
    monkeypatch.setattr(C, '_ACTION_META', ['meta'])
    assert repr(task) == "TASK: meta (test_params)"

def test_task_repr_non_meta(task, monkeypatch):
    monkeypatch.setattr(task, 'get_name', lambda: 'non_meta')
    monkeypatch.setattr(C, '_ACTION_META', ['meta'])
    assert repr(task) == "TASK: non_meta"
