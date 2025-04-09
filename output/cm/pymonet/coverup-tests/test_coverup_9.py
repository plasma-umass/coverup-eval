# file pymonet/task.py:56-72
# lines [56, 66, 67, 68, 69, 72]
# branches []

import pytest
from pymonet.task import Task

def test_task_bind():
    def mapper(value):
        return Task(lambda reject, resolve: resolve(value + 1))

    task = Task(lambda reject, resolve: resolve(1))
    bound_task = task.bind(mapper)

    results = []
    def resolve(value):
        results.append(value)

    def reject(error):
        pytest.fail(f"Unexpected rejection with error: {error}")

    bound_task.fork(reject, resolve)

    assert results == [2], "The bound task should resolve with the correct value"

    # Clean up
    del results[:]
