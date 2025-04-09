# file: lib/ansible/plugins/strategy/linear.py:54-64
# asked: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 59], [62, 63]]}
# gained: {"lines": [54, 55, 56, 58, 59, 60, 61, 62, 63, 64], "branches": [[55, 56], [55, 58], [59, 60], [59, 64], [60, 61], [60, 62], [62, 63]]}

import pytest
from ansible.plugins.strategy.linear import StrategyModule
from ansible.errors import AnsibleAssertionError
from ansible.playbook.task import Task
from ansible.playbook.block import Block

@pytest.fixture
def strategy_module():
    class MockStrategyModule(StrategyModule):
        def __init__(self):
            self.noop_task = Task()
            self._create_noop_block_from = lambda block, parent: Block()
    return MockStrategyModule()

def test_replace_with_noop_noop_task_none():
    class MockStrategyModule(StrategyModule):
        def __init__(self):
            self.noop_task = None

    strategy = MockStrategyModule()
    with pytest.raises(AnsibleAssertionError, match='strategy.linear.StrategyModule.noop_task is None, need Task()'):
        strategy._replace_with_noop([])

def test_replace_with_noop_task(strategy_module):
    task = Task()
    result = strategy_module._replace_with_noop([task])
    assert result == [strategy_module.noop_task]

def test_replace_with_noop_block(strategy_module):
    block = Block()
    result = strategy_module._replace_with_noop([block])
    assert len(result) == 1
    assert isinstance(result[0], Block)
