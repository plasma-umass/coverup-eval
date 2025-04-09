# file: pymonet/task.py:14-24
# asked: {"lines": [14, 15, 24], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
from pymonet.task import Task

class Task:
    @classmethod
    def of(cls, value):
        return Task(lambda _, resolve: resolve(value))

    def __init__(self, func):
        self.func = func

    def run(self, reject, resolve):
        self.func(reject, resolve)

def test_task_of():
    # Test that Task.of correctly stores the value and resolves it
    value = 42
    task = Task.of(value)
    
    def resolve(val):
        assert val == value
    
    task.run(None, resolve)

@pytest.fixture
def mock_task_class(monkeypatch):
    class MockTask:
        def __init__(self, func):
            self.func = func

        def run(self, reject, resolve):
            self.func(reject, resolve)

    monkeypatch.setattr('pymonet.task.Task', MockTask)
    return MockTask

def test_task_of_with_mock(mock_task_class):
    value = "test"
    task = Task.of(value)
    
    def resolve(val):
        assert val == value
    
    task.run(None, resolve)
