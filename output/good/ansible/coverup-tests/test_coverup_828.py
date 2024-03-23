# file lib/ansible/executor/task_result.py:50-51
# lines [50, 51]
# branches []

import pytest
from ansible.executor.task_result import TaskResult

# Mock class to simulate TaskResult's behavior
class MockTaskResult(TaskResult):
    def __init__(self, changed):
        self.changed = changed

    def _check_key(self, key):
        return getattr(self, key, False)

# Test function to cover is_changed method
def test_is_changed():
    # Test when 'changed' is True
    mock_result_true = MockTaskResult(changed=True)
    assert mock_result_true.is_changed() is True

    # Test when 'changed' is False
    mock_result_false = MockTaskResult(changed=False)
    assert mock_result_false.is_changed() is False
