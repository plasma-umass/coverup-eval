# file: lib/ansible/playbook/task.py:136-139
# asked: {"lines": [136, 137, 138, 139], "branches": []}
# gained: {"lines": [136, 137, 138, 139], "branches": []}

import pytest
from ansible.playbook.task import Task

def test_task_load(monkeypatch):
    # Mock the load_data method to avoid side effects
    def mock_load_data(self, data, variable_manager=None, loader=None):
        return "mocked_data"

    monkeypatch.setattr(Task, "load_data", mock_load_data)

    data = {"some": "data"}
    block = "block"
    role = "role"
    task_include = "task_include"
    variable_manager = "variable_manager"
    loader = "loader"

    # Call the static method Task.load
    result = Task.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    # Assertions to verify the postconditions
    assert result == "mocked_data"
    assert isinstance(result, str)
