# file pymonet/task.py:56-72
# lines [56, 66, 67, 68, 69, 72]
# branches []

import pytest
from pymonet.task import Task

def test_task_bind():
    # Define a sample function to bind
    def sample_fn(value):
        def inner_fork(reject, resolve):
            resolve(value + 1)
        return Task(inner_fork)

    # Create a Task instance with a simple fork function
    def initial_fork(reject, resolve):
        resolve(1)
    task = Task(initial_fork)

    # Bind the sample function to the task
    new_task = task.bind(sample_fn)

    # Define reject and resolve functions for testing
    def reject_fn(arg):
        raise Exception(f"Rejected with {arg}")

    def resolve_fn(arg):
        assert arg == 2  # We expect the value to be 2 after binding

    # Call the fork method of the new task
    new_task.fork(reject_fn, resolve_fn)
