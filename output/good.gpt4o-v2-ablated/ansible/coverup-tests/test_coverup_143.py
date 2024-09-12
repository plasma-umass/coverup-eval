# file: lib/ansible/playbook/task.py:91-104
# asked: {"lines": [91, 94, 95, 96, 97, 99, 100, 102, 104], "branches": [[99, 100], [99, 102]]}
# gained: {"lines": [91, 94, 95, 96, 97, 99, 100, 102, 104], "branches": [[99, 100], [99, 102]]}

import pytest
from ansible.playbook.task import Task

def test_task_initialization_with_task_include():
    task_include = "task_include"
    task = Task(task_include=task_include)
    
    assert task._role is None
    assert task._parent == task_include
    assert task.implicit is False
    assert task.resolved_action is None

def test_task_initialization_with_block():
    block = "block"
    task = Task(block=block)
    
    assert task._role is None
    assert task._parent == block
    assert task.implicit is False
    assert task.resolved_action is None

def test_task_initialization_with_role():
    role = "role"
    task = Task(role=role)
    
    assert task._role == role
    assert task._parent is None
    assert task.implicit is False
    assert task.resolved_action is None
