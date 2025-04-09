# file: lib/ansible/plugins/strategy/linear.py:54-64
# asked: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 59], [62, 63]]}
# gained: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 63]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.plugins.strategy.linear import StrategyModule
from unittest.mock import Mock

class MockTask(Task):
    pass

class MockBlock(Block):
    def __init__(self, parent=None):
        self._parent = parent
        self._uuid = "mock-uuid"

@pytest.fixture
def strategy_module():
    tqm_mock = Mock()
    tqm_mock.get_inventory.return_value = Mock()
    tqm_mock._workers = Mock()
    tqm_mock.get_variable_manager.return_value = Mock()
    tqm_mock.get_loader.return_value = Mock()
    tqm_mock._final_q = Mock()
    strategy = StrategyModule(tqm_mock)
    strategy.noop_task = MockTask()
    return strategy

def test_replace_with_noop_raises_error_when_noop_task_is_none():
    tqm_mock = Mock()
    tqm_mock.get_inventory.return_value = Mock()
    tqm_mock._workers = Mock()
    tqm_mock.get_variable_manager.return_value = Mock()
    tqm_mock.get_loader.return_value = Mock()
    tqm_mock._final_q = Mock()
    strategy = StrategyModule(tqm_mock)
    strategy.noop_task = None
    with pytest.raises(AnsibleAssertionError, match='strategy.linear.StrategyModule.noop_task is None, need Task()'):
        strategy._replace_with_noop([])

def test_replace_with_noop_replaces_tasks(monkeypatch, strategy_module):
    task1 = MockTask()
    task2 = MockTask()
    result = strategy_module._replace_with_noop([task1, task2])
    assert result == [strategy_module.noop_task, strategy_module.noop_task]

def test_replace_with_noop_replaces_blocks(monkeypatch, strategy_module):
    block1 = MockBlock()
    block2 = MockBlock()
    
    def mock_create_noop_block_from(original_block, parent):
        return f"noop_block_from_{original_block._uuid}"
    
    monkeypatch.setattr(strategy_module, "_create_noop_block_from", mock_create_noop_block_from)
    
    result = strategy_module._replace_with_noop([block1, block2])
    assert result == [f"noop_block_from_{block1._uuid}", f"noop_block_from_{block2._uuid}"]

def test_replace_with_noop_mixed_elements(monkeypatch, strategy_module):
    task = MockTask()
    block = MockBlock()
    
    def mock_create_noop_block_from(original_block, parent):
        return f"noop_block_from_{original_block._uuid}"
    
    monkeypatch.setattr(strategy_module, "_create_noop_block_from", mock_create_noop_block_from)
    
    result = strategy_module._replace_with_noop([task, block])
    assert result == [strategy_module.noop_task, f"noop_block_from_{block._uuid}"]
