# file: pymonet/task.py:56-72
# asked: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}
# gained: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}

import pytest
from pymonet.task import Task

def test_task_bind():
    # Mock functions for testing
    def mock_fork(reject, resolve):
        resolve(10)

    def mock_fn(value):
        def new_fork(reject, resolve):
            resolve(value + 5)
        return Task(new_fork)

    # Create a Task instance with the mock_fork function
    task = Task(mock_fork)

    # Bind the mock_fn to the task
    new_task = task.bind(mock_fn)

    # Define reject and resolve handlers
    def reject_handler(reason):
        assert False, f"Task was rejected with reason: {reason}"

    def resolve_handler(value):
        assert value == 15, f"Task was resolved with value: {value}"

    # Fork the new task and check the result
    new_task.fork(reject_handler, resolve_handler)
