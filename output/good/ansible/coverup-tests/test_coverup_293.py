# file lib/ansible/executor/task_result.py:96-106
# lines [96, 99, 100, 102, 103, 104, 105, 106]
# branches ['99->100', '99->102', '103->104', '103->106', '104->103', '104->105']

import pytest
from ansible.executor.task_result import TaskResult

# Mock TaskResult class to avoid dependencies on the rest of the Ansible codebase
class MockTaskResult(TaskResult):
    def __init__(self, result):
        self._result = result

@pytest.fixture
def mock_task_result():
    # Fixture to create a TaskResult object with a clean state for each test
    return MockTaskResult

def test_check_key_with_dict_result(mock_task_result):
    result = {'changed': True}
    task_result = mock_task_result(result)
    assert task_result._check_key('changed') is True
    assert task_result._check_key('failed') is False

def test_check_key_with_list_of_dicts_result(mock_task_result):
    result = {'results': [{'changed': True}, {'changed': False}]}
    task_result = mock_task_result(result)
    assert task_result._check_key('changed') is True

def test_check_key_with_list_of_mixed_results(mock_task_result):
    result = {'results': [{'changed': True}, 'not_a_dict']}
    task_result = mock_task_result(result)
    assert task_result._check_key('changed') is True

def test_check_key_with_no_results_key(mock_task_result):
    result = {'not_results': [{'changed': True}]}
    task_result = mock_task_result(result)
    assert task_result._check_key('changed') is False

def test_check_key_with_empty_results(mock_task_result):
    result = {'results': []}
    task_result = mock_task_result(result)
    assert task_result._check_key('changed') is False
