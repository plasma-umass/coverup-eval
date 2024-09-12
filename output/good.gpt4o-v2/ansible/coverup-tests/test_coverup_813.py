# file: lib/ansible/executor/task_result.py:50-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest
from ansible.executor.task_result import TaskResult

def test_is_changed_with_changed_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"changed": True}
    task_result = TaskResult(host, task, return_data)
    
    assert task_result.is_changed() is True

def test_is_changed_without_changed_key():
    host = "localhost"
    task = "dummy_task"
    return_data = {"changed": False}
    task_result = TaskResult(host, task, return_data)
    
    assert task_result.is_changed() is False

def test_is_changed_with_results_list():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": [{"changed": True}, {"changed": False}]}
    task_result = TaskResult(host, task, return_data)
    
    assert task_result.is_changed() is True

def test_is_changed_with_empty_results_list():
    host = "localhost"
    task = "dummy_task"
    return_data = {"results": []}
    task_result = TaskResult(host, task, return_data)
    
    assert task_result.is_changed() is False
