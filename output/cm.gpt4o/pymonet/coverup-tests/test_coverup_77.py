# file pymonet/task.py:38-54
# lines [38, 48, 49, 50, 51, 54]
# branches []

import pytest
from pymonet.task import Task

def test_task_map(mocker):
    # Define a sample function to map
    def sample_fn(x):
        return x * 2

    # Create a Task instance with a dummy function
    def dummy_fork(reject, resolve):
        resolve(10)

    task = Task(dummy_fork)

    # Mock the fork method to control its behavior
    mock_fork = mocker.patch.object(task, 'fork', autospec=True)

    # Call the map method
    new_task = task.map(sample_fn)

    # Ensure the new task is an instance of Task
    assert isinstance(new_task, Task)

    # Define mock reject and resolve functions
    mock_reject = mocker.Mock()
    mock_resolve = mocker.Mock()

    # Call the fork method of the new task
    new_task.fork(mock_reject, mock_resolve)

    # Ensure the original fork method was called with the correct arguments
    mock_fork.side_effect = lambda reject, resolve: resolve(10)
    new_task.fork(mock_reject, mock_resolve)

    # Ensure the resolve function was called with the mapped value
    mock_resolve.assert_called_once_with(20)

    # Ensure the reject function was not called
    mock_reject.assert_not_called()
