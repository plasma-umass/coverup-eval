# file: pymonet/task.py:56-72
# asked: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}
# gained: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}

import pytest
from pymonet.task import Task

def test_task_bind_executes_all_lines_and_branches(monkeypatch):
    # Mock function to be used with bind
    def mock_fn(value):
        return Task(lambda reject, resolve: resolve(value + 1))

    # Mock fork function to be used in Task
    def mock_fork(reject, resolve):
        resolve(10)

    # Create a Task instance with the mock fork function
    task = Task(mock_fork)

    # Bind the mock function to the task
    new_task = task.bind(mock_fn)

    # Assertions to verify the postconditions
    def mock_reject(arg):
        assert False, "Reject should not be called"

    def mock_resolve(arg):
        assert arg == 11, "Resolve should be called with the incremented value"

    # Execute the new task's fork function to ensure all lines and branches are covered
    new_task.fork(mock_reject, mock_resolve)
