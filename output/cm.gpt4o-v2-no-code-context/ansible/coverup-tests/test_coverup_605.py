# file: lib/ansible/playbook/task_include.py:104-107
# asked: {"lines": [104, 105, 106, 107], "branches": []}
# gained: {"lines": [104, 105, 106, 107], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude

class MockTask:
    def copy(self, exclude_parent=False, exclude_tasks=False):
        return self

@pytest.fixture
def task_include(monkeypatch):
    monkeypatch.setattr('ansible.playbook.task_include.Task', MockTask)
    task = TaskInclude()
    task.statically_loaded = True
    return task

def test_task_include_copy(task_include):
    new_task = task_include.copy()
    assert new_task.statically_loaded == task_include.statically_loaded

def test_task_include_copy_exclude_parent(task_include):
    new_task = task_include.copy(exclude_parent=True)
    assert new_task.statically_loaded == task_include.statically_loaded

def test_task_include_copy_exclude_tasks(task_include):
    new_task = task_include.copy(exclude_tasks=True)
    assert new_task.statically_loaded == task_include.statically_loaded

def test_task_include_copy_exclude_both(task_include):
    new_task = task_include.copy(exclude_parent=True, exclude_tasks=True)
    assert new_task.statically_loaded == task_include.statically_loaded
