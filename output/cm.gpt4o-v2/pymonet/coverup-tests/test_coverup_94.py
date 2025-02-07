# file: pymonet/task.py:38-54
# asked: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}
# gained: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}

import pytest
from pymonet.task import Task

def test_task_map():
    def fork(reject, resolve):
        resolve(10)

    def mapper(x):
        return x * 2

    task = Task(fork)
    new_task = task.map(mapper)

    assert isinstance(new_task, Task)

    def resolve_callback(x):
        assert x == 20

    new_task.fork(lambda x: None, resolve_callback)

def test_task_map_reject():
    def fork(reject, resolve):
        reject("error")

    def mapper(x):
        return x * 2

    task = Task(fork)
    new_task = task.map(mapper)

    assert isinstance(new_task, Task)

    def reject_callback(x):
        assert x == "error"

    new_task.fork(reject_callback, lambda x: None)
