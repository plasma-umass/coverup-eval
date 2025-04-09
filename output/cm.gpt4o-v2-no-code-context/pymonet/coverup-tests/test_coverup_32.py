# file: pymonet/task.py:38-54
# asked: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}
# gained: {"lines": [38, 48, 49, 50, 51, 54], "branches": []}

import pytest
from pymonet.task import Task

def test_task_map_function_executes_correctly():
    def sample_fork(reject, resolve):
        resolve(10)

    task = Task(sample_fork)
    
    def mapper_function(x):
        return x * 2

    new_task = task.map(mapper_function)

    def mock_reject(arg):
        assert False, "Reject should not be called"

    def mock_resolve(arg):
        assert arg == 20

    new_task.fork(mock_reject, mock_resolve)

def test_task_map_function_reject():
    def sample_fork(reject, resolve):
        reject("error")

    task = Task(sample_fork)
    
    def mapper_function(x):
        return x * 2

    new_task = task.map(mapper_function)

    def mock_reject(arg):
        assert arg == "error"

    def mock_resolve(arg):
        assert False, "Resolve should not be called"

    new_task.fork(mock_reject, mock_resolve)
