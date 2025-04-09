# file: pymonet/task.py:14-24
# asked: {"lines": [14, 15, 24], "branches": []}
# gained: {"lines": [14, 15, 24], "branches": []}

import pytest
from pymonet.task import Task

def test_task_of():
    # Create a Task using the `of` class method
    value = 42
    task = Task.of(value)
    
    # Ensure the task is an instance of Task
    assert isinstance(task, Task)
    
    # Define a resolve function to capture the resolved value
    resolved_value = None
    def resolve(val):
        nonlocal resolved_value
        resolved_value = val
    
    # Call the fork method of the task to resolve it
    task.fork(None, resolve)
    
    # Ensure the resolved value is the same as the input value
    assert resolved_value == value
