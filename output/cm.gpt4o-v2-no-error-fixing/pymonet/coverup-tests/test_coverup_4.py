# file: pymonet/task.py:56-72
# asked: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}
# gained: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}

import pytest
from pymonet.task import Task

def test_task_bind():
    def mock_fork(reject, resolve):
        resolve(10)

    def mapper_function(value):
        return Task(lambda reject, resolve: resolve(value * 2))

    task = Task(mock_fork)
    new_task = task.bind(mapper_function)

    def result_reject(arg):
        assert False, "This should not be called"

    def result_resolve(arg):
        assert arg == 20

    new_task.fork(result_reject, result_resolve)
