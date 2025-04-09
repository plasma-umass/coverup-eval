# file: lib/ansible/playbook/task.py:441-451
# asked: {"lines": [441, 448, 450, 451], "branches": [[450, 0], [450, 451]]}
# gained: {"lines": [441, 448, 450, 451], "branches": [[450, 0], [450, 451]]}

import pytest
from ansible.playbook.task import Task
from unittest.mock import Mock

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_parent():
    parent = Mock()
    parent.set_loader = Mock()
    return parent

def test_set_loader_with_parent(mock_loader, mock_parent):
    task = Task()
    task._parent = mock_parent
    task.set_loader(mock_loader)
    
    assert task._loader == mock_loader
    mock_parent.set_loader.assert_called_once_with(mock_loader)

def test_set_loader_without_parent(mock_loader):
    task = Task()
    task._parent = None
    task.set_loader(mock_loader)
    
    assert task._loader == mock_loader
