# file: lib/ansible/playbook/block.py:361-387
# asked: {"lines": [361, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 370], [369, 373], [371, 368], [371, 372], [373, 368], [373, 376]]}
# gained: {"lines": [361, 366, 367, 368, 369, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 373], [373, 376]]}

import pytest
from ansible.playbook.block import Block
from ansible.playbook.task import Task
import ansible.constants as C

class MockPlay:
    def __init__(self, only_tags=None, skip_tags=None):
        self.only_tags = only_tags or []
        self.skip_tags = skip_tags or []

class MockTask:
    def __init__(self, action, implicit=False):
        self.action = action
        self.implicit = implicit

    def evaluate_tags(self, only_tags, skip_tags, all_vars=None):
        return True

@pytest.fixture
def mock_play():
    return MockPlay()

@pytest.fixture
def block(mock_play):
    return Block(play=mock_play)

def test_filter_tagged_tasks(block, mock_play):
    task1 = MockTask(action='meta', implicit=True)
    task2 = MockTask(action='include')
    task3 = MockTask(action='other')

    block.block = [task1, task2, task3]
    block.rescue = [task1]
    block.always = [task2]

    filtered_block = block.filter_tagged_tasks(all_vars={})

    assert len(filtered_block.block) == 3
    assert len(filtered_block.rescue) == 1
    assert len(filtered_block.always) == 1
    assert filtered_block.block[0].action == 'meta'
    assert filtered_block.block[1].action == 'include'
    assert filtered_block.block[2].action == 'other'
