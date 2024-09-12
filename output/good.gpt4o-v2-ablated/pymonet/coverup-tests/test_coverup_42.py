# file: pymonet/task.py:7-12
# asked: {"lines": [7, 12], "branches": []}
# gained: {"lines": [7, 12], "branches": []}

import pytest

from pymonet.task import Task

def test_task_initialization():
    def dummy_fork(reject, resolve):
        pass

    task = Task(dummy_fork)
    assert task.fork == dummy_fork
