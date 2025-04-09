# file pymonet/task.py:38-54
# lines [38, 48, 49, 50, 51, 54]
# branches []

import pytest
from pymonet.task import Task

def test_task_map():
    # Helper functions to simulate resolve and reject
    def resolve(value):
        return 'resolved with ' + str(value)

    def reject(value):
        return 'rejected with ' + str(value)

    # Function to be mapped over the Task
    def increment(x):
        return x + 1

    # Create a Task that resolves with a value
    task = Task(lambda reject, resolve: resolve(1))

    # Map the increment function over the Task
    mapped_task = task.map(increment)

    # Ensure that the mapped Task resolves with the incremented value
    assert mapped_task.fork(reject, resolve) == 'resolved with 2'

    # Create a Task that rejects with a value
    rejected_task = Task(lambda reject, resolve: reject('error'))

    # Map the increment function over the rejected Task
    mapped_rejected_task = rejected_task.map(increment)

    # Ensure that the mapped Task still rejects with the original error
    assert mapped_rejected_task.fork(reject, resolve) == 'rejected with error'
