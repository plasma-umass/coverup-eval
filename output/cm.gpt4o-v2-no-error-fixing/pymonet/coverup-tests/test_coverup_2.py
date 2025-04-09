# file: pymonet/task.py:38-54
# asked: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}
# gained: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}

import pytest
from pymonet.task import Task

def test_task_map():
    # Mock function to be used with map
    def mock_function(x):
        return x * 2

    # Mock fork function
    def mock_fork(reject, resolve):
        resolve(10)

    # Create a Task instance with the mock fork function
    task = Task(mock_fork)

    # Use the map method
    new_task = task.map(mock_function)

    # Mock reject and resolve functions
    def mock_reject(x):
        assert False, "Reject should not be called"

    def mock_resolve(x):
        assert x == 20, "Resolve should be called with the mapped value"

    # Call the fork method of the new task to trigger the map logic
    new_task.fork(mock_reject, mock_resolve)
