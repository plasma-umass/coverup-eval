# file pymonet/task.py:14-24
# lines [24]
# branches []

import pytest
from pymonet.task import Task

def test_task_of_executes_line_24():
    value = "test_value"
    task = Task.of(value)
    result = None

    def on_success(resolved_value):
        nonlocal result
        result = resolved_value

    task.fork(None, on_success)
    assert result == value
