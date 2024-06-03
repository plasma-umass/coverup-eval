# file lib/ansible/playbook/task.py:91-104
# lines [91, 94, 95, 96, 97, 99, 100, 102, 104]
# branches ['99->100', '99->102']

import pytest
from ansible.playbook.task import Task

def test_task_initialization_with_task_include():
    task_include = object()
    task = Task(task_include=task_include)
    
    assert task._parent is task_include
    assert task._role is None
    assert task.implicit is False
    assert task.resolved_action is None

def test_task_initialization_with_block():
    block = object()
    task = Task(block=block)
    
    assert task._parent is block
    assert task._role is None
    assert task.implicit is False
    assert task.resolved_action is None

def test_task_initialization_with_role():
    role = object()
    task = Task(role=role)
    
    assert task._role is role
    assert task._parent is None
    assert task.implicit is False
    assert task.resolved_action is None

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
