# file: pymonet/task.py:38-54
# asked: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}
# gained: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}

import pytest
from pymonet.task import Task

def test_task_map():
    # Mock function to be used with map
    def mock_fn(x):
        return x + 1

    # Mock fork function
    def mock_fork(reject, resolve):
        resolve(1)

    # Create a Task instance with the mock fork function
    task = Task(mock_fork)

    # Map the mock function to the task
    new_task = task.map(mock_fn)

    # Assert that the new task is an instance of Task
    assert isinstance(new_task, Task)

    # Mock reject and resolve functions
    def mock_reject(x):
        pass

    def mock_resolve(x):
        assert x == 2  # Since mock_fn adds 1, the result should be 2

    # Call the fork function of the new task
    new_task.fork(mock_reject, mock_resolve)
