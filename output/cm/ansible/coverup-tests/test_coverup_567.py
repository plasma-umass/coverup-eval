# file lib/ansible/playbook/task.py:441-451
# lines [441, 448, 450, 451]
# branches ['450->exit', '450->451']

import pytest
from ansible.playbook.task import Task
from ansible.parsing.dataloader import DataLoader

class MockParent:
    def __init__(self):
        self.loader_set = False

    def set_loader(self, loader):
        self.loader_set = True

@pytest.fixture
def mock_loader(mocker):
    return mocker.Mock(spec=DataLoader)

@pytest.fixture
def task_with_parent(mock_loader):
    task = Task()
    task._parent = MockParent()
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    return task

def test_set_loader_with_parent(task_with_parent, mock_loader):
    task_with_parent.set_loader(mock_loader)
    assert task_with_parent._loader is mock_loader
    assert task_with_parent._parent.loader_set is True

def test_set_loader_without_parent(task_without_parent, mock_loader):
    task_without_parent.set_loader(mock_loader)
    assert task_without_parent._loader is mock_loader
    assert task_without_parent._parent is None
