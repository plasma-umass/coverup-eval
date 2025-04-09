# file: lib/ansible/playbook/task_include.py:53-61
# asked: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

class MockTask(Task):
    def __init__(self, block=None, role=None, task_include=None):
        self._block = block
        self._role = role
        self._task_include = task_include
        self.statically_loaded = False

    def check_options(self, task, data):
        return task

    def load_data(self, data, variable_manager=None, loader=None):
        return data

@pytest.fixture
def mock_task_include(monkeypatch):
    monkeypatch.setattr(TaskInclude, "__init__", MockTask.__init__)
    monkeypatch.setattr(TaskInclude, "check_options", MockTask.check_options)
    monkeypatch.setattr(TaskInclude, "load_data", MockTask.load_data)

def test_task_include_load(mock_task_include):
    data = {"key": "value"}
    block = "block"
    role = "role"
    task_include = "task_include"
    variable_manager = "variable_manager"
    loader = "loader"

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task == data
