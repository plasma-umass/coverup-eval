# file: lib/ansible/executor/task_result.py:96-106
# asked: {"lines": [96, 99, 100, 102, 103, 104, 105, 106], "branches": [[99, 100], [99, 102], [103, 104], [103, 106], [104, 103], [104, 105]]}
# gained: {"lines": [96, 99, 100, 102, 103, 104, 105, 106], "branches": [[99, 100], [99, 102], [103, 104], [103, 106], [104, 105]]}

import pytest
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result_dict():
    return TaskResult(host="localhost", task="dummy_task", return_data={"key1": "value1", "key2": "value2"})

@pytest.fixture
def task_result_list():
    return TaskResult(host="localhost", task="dummy_task", return_data={"results": [{"key1": True}, {"key2": True}]})

def test_check_key_in_dict(task_result_dict):
    assert task_result_dict._check_key("key1") == "value1"
    assert task_result_dict._check_key("key2") == "value2"
    assert task_result_dict._check_key("key3") is False

def test_check_key_in_list(task_result_list):
    assert task_result_list._check_key("key1") is True
    assert task_result_list._check_key("key2") is True
    assert task_result_list._check_key("key3") is False
