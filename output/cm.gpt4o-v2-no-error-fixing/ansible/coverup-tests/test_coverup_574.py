# file: lib/ansible/executor/task_result.py:72-73
# asked: {"lines": [72, 73], "branches": []}
# gained: {"lines": [72, 73], "branches": []}

import pytest
from ansible.executor.task_result import TaskResult

def test_is_unreachable_with_direct_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"unreachable": True}
    task_result = TaskResult(host, task, return_data)

    assert task_result.is_unreachable() is True

def test_is_unreachable_with_nested_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"unreachable": True}]}
    task_result = TaskResult(host, task, return_data)

    assert task_result.is_unreachable() is True

def test_is_unreachable_with_no_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"unreachable": False}]}
    task_result = TaskResult(host, task, return_data)

    assert task_result.is_unreachable() is False
