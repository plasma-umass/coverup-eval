# file: pymonet/task.py:14-24
# asked: {"lines": [14, 15, 24], "branches": []}
# gained: {"lines": [14, 15, 24], "branches": []}

import pytest
from pymonet.task import Task

def test_task_of():
    value = 42
    task = Task.of(value)
    
    def resolve(val):
        assert val == value

    task.fork(None, resolve)
