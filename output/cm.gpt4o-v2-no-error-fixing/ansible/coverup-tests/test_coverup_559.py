# file: lib/ansible/executor/task_result.py:50-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    host = "localhost"
    task = "dummy_task"
    return_data = {"changed": True}
    return TaskResult(host, task, return_data)

def test_is_changed(task_result):
    assert task_result.is_changed() == True

def test_is_changed_with_no_changed_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"changed": False}, {"changed": True}]}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_changed() == True

def test_is_changed_with_no_results_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_changed() == False
