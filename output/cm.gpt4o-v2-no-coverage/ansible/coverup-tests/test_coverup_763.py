# file: lib/ansible/playbook/task_include.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

@pytest.fixture
def task_include_instance():
    return TaskInclude()

def test_task_include_init(task_include_instance):
    assert isinstance(task_include_instance, TaskInclude)
    assert not task_include_instance.statically_loaded

def test_task_include_super_init(monkeypatch):
    def mock_init(self, block=None, role=None, task_include=None):
        self.block = block
        self.role = role
        self.task_include = task_include

    monkeypatch.setattr(Task, '__init__', mock_init)
    instance = TaskInclude(block='block', role='role', task_include='task_include')
    assert instance.block == 'block'
    assert instance.role == 'role'
    assert instance.task_include == 'task_include'
    assert not instance.statically_loaded
