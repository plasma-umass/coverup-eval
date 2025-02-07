# file: pymonet/task.py:14-24
# asked: {"lines": [14, 15, 24], "branches": []}
# gained: {"lines": [14, 15, 24], "branches": []}

import pytest
from pymonet.task import Task

def test_task_of():
    # Create a Task with a specific value
    value = 42
    task = Task.of(value)
    
    # Ensure the task is created correctly
    assert isinstance(task, Task)
    
    # Mock the resolve function to capture the resolved value
    resolved_value = None
    def mock_resolve(val):
        nonlocal resolved_value
        resolved_value = val
    
    # Execute the task to resolve the value
    task.fork(None, mock_resolve)
    
    # Verify the resolved value is as expected
    assert resolved_value == value
