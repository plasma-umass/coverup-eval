# file: lib/ansible/executor/task_result.py:50-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def task_result_dict():
    return TaskResult(host="localhost", task="dummy_task", return_data={"changed": True})

@pytest.fixture
def task_result_list():
    return TaskResult(host="localhost", task="dummy_task", return_data={"results": [{"changed": True}, {"changed": False}]})

def test_is_changed_dict(task_result_dict):
    assert task_result_dict.is_changed() is True

def test_is_changed_list(task_result_list):
    assert task_result_list.is_changed() is True

def test_is_changed_not_present():
    tr = TaskResult(host="localhost", task="dummy_task", return_data={"results": [{"failed": True}, {"skipped": False}]})
    assert tr.is_changed() is False
