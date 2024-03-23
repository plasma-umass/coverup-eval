# file lib/ansible/executor/task_result.py:72-73
# lines [72, 73]
# branches []

import pytest
from ansible.executor.task_result import TaskResult

# Mock class to simulate TaskResult behavior
class MockTaskResult(TaskResult):
    def __init__(self, unreachable=False):
        self._result = {'unreachable': unreachable} if unreachable else {}

    def _check_key(self, key):
        return key in self._result and bool(self._result[key])

# Test function to cover is_unreachable method
def test_is_unreachable():
    # Test when the result is not unreachable
    task_result_not_unreachable = MockTaskResult(unreachable=False)
    assert not task_result_not_unreachable.is_unreachable()

    # Test when the result is unreachable
    task_result_unreachable = MockTaskResult(unreachable=True)
    assert task_result_unreachable.is_unreachable()
