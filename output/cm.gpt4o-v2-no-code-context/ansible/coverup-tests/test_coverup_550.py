# file: lib/ansible/playbook/task.py:141-146
# asked: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}
# gained: {"lines": [141, 143, 144, 146], "branches": [[143, 144], [143, 146]]}

import pytest
from ansible.playbook.task import Task
from unittest.mock import MagicMock

class MockTask(Task):
    def __init__(self, name, args):
        self._name = name
        self.args = args
        self._squashed = False
        self._finalized = False

    def get_name(self):
        return self._name

@pytest.fixture
def mock_task_meta():
    return MockTask(name='meta', args={'_raw_params': 'some_params'})

@pytest.fixture
def mock_task_regular():
    return MockTask(name='regular_task', args={})

def test_task_repr_meta(mock_task_meta, monkeypatch):
    monkeypatch.setattr('ansible.constants._ACTION_META', ['meta'])
    result = repr(mock_task_meta)
    assert result == "TASK: meta (some_params)"

def test_task_repr_regular(mock_task_regular, monkeypatch):
    monkeypatch.setattr('ansible.constants._ACTION_META', ['meta'])
    result = repr(mock_task_regular)
    assert result == "TASK: regular_task"
