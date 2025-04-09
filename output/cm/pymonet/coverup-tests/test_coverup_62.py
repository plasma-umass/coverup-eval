# file pymonet/task.py:7-12
# lines [7, 12]
# branches []

import pytest
from pymonet.task import Task

def test_task_initialization():
    def fork_function(reject, resolve):
        # This function will be passed to the Task constructor
        # but we don't need to do anything with it for this test.
        pass

    task = Task(fork_function)
    assert task.fork == fork_function

def test_task_fork_execution(mocker):
    # Mock the fork function to ensure it's called with correct arguments
    mock_fork = mocker.Mock()

    # Create a Task with the mocked fork function
    task = Task(mock_fork)

    # Prepare the reject and resolve functions
    reject = mocker.Mock()
    resolve = mocker.Mock()

    # Execute the fork function within the Task
    task.fork(reject, resolve)

    # Assert that the fork function was called with the reject and resolve functions
    mock_fork.assert_called_once_with(reject, resolve)

    # Clean up is not necessary as we are using mocks and they are function-scoped
