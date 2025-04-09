# file lib/ansible/playbook/block.py:50-63
# lines [59, 61]
# branches ['58->59', '60->61']

import pytest
from ansible.playbook.block import Block

# Mock classes to pass as parameters to Block
class MockPlay:
    pass

class MockTaskInclude:
    pass

class MockParentBlock:
    pass

@pytest.fixture
def mock_play():
    return MockPlay()

@pytest.fixture
def mock_task_include():
    return MockTaskInclude()

@pytest.fixture
def mock_parent_block():
    return MockParentBlock()

def test_block_with_task_include(mock_play, mock_task_include):
    block = Block(play=mock_play, task_include=mock_task_include)
    assert block._parent is mock_task_include

def test_block_with_parent_block(mock_play, mock_parent_block):
    block = Block(play=mock_play, parent_block=mock_parent_block)
    assert block._parent is mock_parent_block
