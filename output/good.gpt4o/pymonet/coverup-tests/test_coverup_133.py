# file pymonet/task.py:14-24
# lines [24]
# branches []

import pytest
from pymonet.task import Task

def test_task_of_resolves_value():
    # Arrange
    value = 42

    # Act
    task = Task.of(value)
    result = []
    task.fork(lambda x: None, lambda x: result.append(x))

    # Assert
    assert result == [value]
