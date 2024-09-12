# file: lib/ansible/executor/task_result.py:72-73
# asked: {"lines": [72, 73], "branches": []}
# gained: {"lines": [72, 73], "branches": []}

import pytest
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    host = "localhost"
    task = "dummy_task"
    return_data = {"unreachable": True}
    return TaskResult(host, task, return_data)

def test_is_unreachable(task_result):
    assert task_result.is_unreachable() is True

def test_is_unreachable_with_no_unreachable_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"unreachable": False}, {"unreachable": False}]}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_unreachable() is False

def test_is_unreachable_with_unreachable_in_results():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"unreachable": True}, {"unreachable": False}]}
    task_result = TaskResult(host, task, return_data)
    assert task_result.is_unreachable() is True
