# file: lib/ansible/playbook/task.py:441-451
# asked: {"lines": [441, 448, 450, 451], "branches": [[450, 0], [450, 451]]}
# gained: {"lines": [441, 448, 450, 451], "branches": [[450, 0], [450, 451]]}

import pytest
from ansible.playbook.task import Task

class MockParent:
    def __init__(self):
        self.loader_set = False

    def set_loader(self, loader):
        self.loader_set = True

def test_set_loader_with_parent():
    parent = MockParent()
    task = Task()
    task._parent = parent
    loader = object()

    task.set_loader(loader)

    assert task._loader == loader
    assert parent.loader_set

def test_set_loader_without_parent():
    task = Task()
    loader = object()

    task.set_loader(loader)

    assert task._loader == loader
