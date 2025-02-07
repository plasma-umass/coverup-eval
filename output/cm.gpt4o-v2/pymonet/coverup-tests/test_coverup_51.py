# file: pymonet/task.py:26-36
# asked: {"lines": [26, 27, 36], "branches": []}
# gained: {"lines": [26, 27, 36], "branches": []}

import pytest
from pymonet.task import Task

def test_task_reject():
    # Create a rejected Task with a specific value
    value = "error"
    task = Task.reject(value)

    # Define a reject function to capture the rejected value
    def reject_fn(rejected_value):
        assert rejected_value == value

    # Define a resolve function that should not be called
    def resolve_fn(_):
        assert False, "Resolve function should not be called for a rejected Task"

    # Execute the task's fork method
    task.fork(reject_fn, resolve_fn)
