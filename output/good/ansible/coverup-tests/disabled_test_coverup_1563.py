# file lib/ansible/plugins/strategy/linear.py:54-64
# lines [55, 56, 58, 59, 60, 61, 62, 63, 64]
# branches ['55->56', '55->58', '59->60', '59->64', '60->61', '60->62', '62->59', '62->63']

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.playbook.block import Block
from ansible.playbook.task import Task
from ansible.plugins.strategy.linear import StrategyModule

class MockTask(Task):
    pass

class MockBlock(Block):
    pass

@pytest.fixture
def strategy_module(mocker):
    mocker.patch('ansible.plugins.strategy.StrategyBase.__init__', return_value=None)
    strategy = StrategyModule()
    strategy.noop_task = MockTask()
    mocker.patch.object(strategy, '_create_noop_block_from', return_value=MockBlock())
    return strategy

def test_replace_with_noop_with_no_noop_task(strategy_module, mocker):
    strategy_module.noop_task = None
    with pytest.raises(AnsibleAssertionError):
        strategy_module._replace_with_noop([MockTask()])

def test_replace_with_noop_with_task(strategy_module):
    result = strategy_module._replace_with_noop([MockTask()])
    assert len(result) == 1
    assert isinstance(result[0], MockTask)

def test_replace_with_noop_with_block(strategy_module):
    result = strategy_module._replace_with_noop([MockBlock()])
    assert len(result) == 1
    assert isinstance(result[0], MockBlock)

def test_replace_with_noop_with_mixed_content(strategy_module):
    result = strategy_module._replace_with_noop([MockTask(), MockBlock()])
    assert len(result) == 2
    assert isinstance(result[0], MockTask)
    assert isinstance(result[1], MockBlock)
