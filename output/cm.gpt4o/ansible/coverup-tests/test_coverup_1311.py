# file lib/ansible/playbook/task.py:441-451
# lines []
# branches ['450->exit']

import pytest
from unittest import mock
from ansible.playbook.task import Task

class MockParent:
    def set_loader(self, loader):
        self.loader = loader

@pytest.fixture
def task_with_parent():
    parent = MockParent()
    task = Task()
    task._parent = parent
    return task, parent

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    return task

def test_set_loader_with_parent(task_with_parent):
    task, parent = task_with_parent
    loader = mock.Mock()
    
    task.set_loader(loader)
    
    assert task._loader == loader
    assert parent.loader == loader

def test_set_loader_without_parent(task_without_parent):
    task = task_without_parent
    loader = mock.Mock()
    
    task.set_loader(loader)
    
    assert task._loader == loader
