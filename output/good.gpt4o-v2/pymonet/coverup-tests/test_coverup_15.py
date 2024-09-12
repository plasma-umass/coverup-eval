# file: pymonet/task.py:56-72
# asked: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}
# gained: {"lines": [56, 66, 67, 68, 69, 72], "branches": []}

import pytest
from pymonet.task import Task

def test_task_bind():
    def mock_fork(reject, resolve):
        resolve(10)

    def mapper(value):
        return Task(lambda reject, resolve: resolve(value + 5))

    task = Task(mock_fork)
    bound_task = task.bind(mapper)

    def result_fork(reject, resolve):
        bound_task.fork(reject, resolve)

    result_task = Task(result_fork)

    def resolve(value):
        assert value == 15

    def reject(value):
        pytest.fail("Reject should not be called")

    result_task.fork(reject, resolve)
