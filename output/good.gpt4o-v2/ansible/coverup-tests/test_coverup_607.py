# file: lib/ansible/plugins/strategy/linear.py:54-64
# asked: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 59], [62, 63]]}
# gained: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 63]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.plugins.strategy.linear import StrategyModule

class MockTQM:
    def get_inventory(self):
        return None

    def get_variable_manager(self):
        return None

    def get_loader(self):
        return None

    @property
    def _workers(self):
        return None

    @property
    def _final_q(self):
        return None

@pytest.fixture
def strategy_module():
    tqm = MockTQM()
    return StrategyModule(tqm)

def test_replace_with_noop_raises_exception_when_noop_task_is_none(strategy_module):
    strategy_module.noop_task = None
    with pytest.raises(AnsibleAssertionError, match='strategy.linear.StrategyModule.noop_task is None, need Task()'):
        strategy_module._replace_with_noop([])

def test_replace_with_noop_replaces_task_with_noop_task(strategy_module):
    noop_task = Task()
    strategy_module.noop_task = noop_task
    task = Task()
    result = strategy_module._replace_with_noop([task])
    assert result == [noop_task]

def test_replace_with_noop_replaces_block_with_noop_block(strategy_module, mocker):
    noop_task = Task()
    strategy_module.noop_task = noop_task
    block = Block()
    mock_create_noop_block_from = mocker.patch.object(strategy_module, '_create_noop_block_from', return_value='noop_block')
    result = strategy_module._replace_with_noop([block])
    mock_create_noop_block_from.assert_called_once_with(block, block._parent)
    assert result == ['noop_block']

def test_replace_with_noop_mixed_elements(strategy_module, mocker):
    noop_task = Task()
    strategy_module.noop_task = noop_task
    task = Task()
    block = Block()
    mock_create_noop_block_from = mocker.patch.object(strategy_module, '_create_noop_block_from', return_value='noop_block')
    result = strategy_module._replace_with_noop([task, block])
    mock_create_noop_block_from.assert_called_once_with(block, block._parent)
    assert result == [noop_task, 'noop_block']
