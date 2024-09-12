# file: lib/ansible/playbook/task.py:141-146
# asked: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}
# gained: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}

import pytest
from ansible.playbook.task import Task
from ansible import constants as C

class MockTask(Task):
    def __init__(self, name, raw_params=None):
        self._name = name
        self.args = {'_raw_params': raw_params}
        self._squashed = False
        self._finalized = False

    def get_name(self):
        return self._name

@pytest.fixture
def task_meta():
    return MockTask(name='meta', raw_params='some_params')

@pytest.fixture
def task_regular():
    return MockTask(name='regular_task')

def test_task_repr_meta(task_meta):
    assert repr(task_meta) == "TASK: meta (some_params)"

def test_task_repr_regular(task_regular):
    assert repr(task_regular) == "TASK: regular_task"
