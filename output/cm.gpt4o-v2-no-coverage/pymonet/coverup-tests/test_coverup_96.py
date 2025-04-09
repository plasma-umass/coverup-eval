# file: pymonet/task.py:26-36
# asked: {"lines": [26, 27, 36], "branches": []}
# gained: {"lines": [26, 27, 36], "branches": []}

import pytest
from pymonet.task import Task

def test_task_reject():
    # Arrange
    value = "error"

    # Act
    rejected_task = Task.reject(value)

    # Assert
    def reject_fn(reject, resolve):
        assert reject == value

    rejected_task.fork(lambda v: reject_fn(v, None), lambda _: None)
