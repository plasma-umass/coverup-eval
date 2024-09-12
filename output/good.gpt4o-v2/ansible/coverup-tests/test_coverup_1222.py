# file: lib/ansible/playbook/block.py:361-387
# asked: {"lines": [370, 371, 372], "branches": [[369, 370], [371, 368], [371, 372]]}
# gained: {"lines": [370, 371, 372], "branches": [[369, 370], [371, 368], [371, 372]]}

import pytest
from ansible.playbook.block import Block
import ansible.constants as C

class MockTask:
    def __init__(self, action, implicit=False):
        self.action = action
        self.implicit = implicit

    def evaluate_tags(self, only_tags, skip_tags, all_vars):
        return True

class MockPlay:
    def __init__(self):
        self.only_tags = []
        self.skip_tags = []

@pytest.fixture
def mock_block():
    play = MockPlay()
    return Block(play=play)

def test_filter_tagged_tasks_with_meta_action(mock_block):
    task = MockTask(action='meta', implicit=True)
    mock_block.block = [task]
    filtered_block = mock_block.filter_tagged_tasks({})
    assert len(filtered_block.block) == 1
    assert filtered_block.block[0].action == 'meta'

def test_filter_tagged_tasks_with_include_action(mock_block):
    task = MockTask(action='include')
    mock_block.block = [task]
    filtered_block = mock_block.filter_tagged_tasks({})
    assert len(filtered_block.block) == 1
    assert filtered_block.block[0].action == 'include'

def test_filter_tagged_tasks_with_evaluate_tags(mock_block):
    task = MockTask(action='some_action')
    mock_block.block = [task]
    filtered_block = mock_block.filter_tagged_tasks({})
    assert len(filtered_block.block) == 1
    assert filtered_block.block[0].action == 'some_action'

def test_filter_tagged_tasks_with_nested_block(mock_block):
    nested_task = MockTask(action='some_action')
    nested_block = Block(play=mock_block._play)
    nested_block.block = [nested_task]
    mock_block.block = [nested_block]
    filtered_block = mock_block.filter_tagged_tasks({})
    assert len(filtered_block.block) == 1
    assert isinstance(filtered_block.block[0], Block)
    assert len(filtered_block.block[0].block) == 1
    assert filtered_block.block[0].block[0].action == 'some_action'

def test_filter_tagged_tasks_with_empty_nested_block(mock_block):
    nested_block = Block(play=mock_block._play)
    mock_block.block = [nested_block]
    filtered_block = mock_block.filter_tagged_tasks({})
    assert len(filtered_block.block) == 0
