# file: lib/ansible/playbook/task_include.py:49-51
# asked: {"lines": [49, 50, 51], "branches": []}
# gained: {"lines": [49, 50, 51], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

class MockTask(Task):
    def __init__(self, block=None, role=None, task_include=None):
        self._role = role
        self._parent = None
        self.implicit = False
        self.resolved_action = None
        if task_include:
            self._parent = task_include
        else:
            self._parent = block
        super(Task, self).__init__()

@pytest.fixture
def mock_task(mocker):
    mocker.patch('ansible.playbook.task_include.Task', MockTask)

def test_task_include_init_with_task_include(mock_task):
    task_include = MockTask()
    task = TaskInclude(task_include=task_include)
    assert task._parent == task_include
    assert task.statically_loaded is False

def test_task_include_init_with_block(mock_task):
    block = MockTask()
    task = TaskInclude(block=block)
    assert task._parent == block
    assert task.statically_loaded is False
