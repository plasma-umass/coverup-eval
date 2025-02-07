# file: lib/ansible/plugins/strategy/linear.py:66-72
# asked: {"lines": [67, 68, 69, 70, 72], "branches": []}
# gained: {"lines": [67, 68, 69, 70, 72], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.block import Block
from ansible.plugins.strategy.linear import StrategyModule

@pytest.fixture
def mock_replace_with_noop(mocker):
    return mocker.patch.object(StrategyModule, '_replace_with_noop', side_effect=lambda x: x)

@pytest.fixture
def mock_tqm():
    return MagicMock()

def test_create_noop_block_from(mock_replace_with_noop, mock_tqm):
    strategy = StrategyModule(mock_tqm)
    original_block = Block()
    original_block.block = ['task1']
    original_block.always = ['task2']
    original_block.rescue = ['task3']
    
    parent_block = Block()
    
    noop_block = strategy._create_noop_block_from(original_block, parent_block)
    
    assert noop_block.block == original_block.block
    assert noop_block.always == original_block.always
    assert noop_block.rescue == original_block.rescue
    assert noop_block._parent == parent_block
