# file lib/ansible/plugins/strategy/linear.py:54-64
# lines [54, 55, 56, 58, 59, 60, 61, 62, 63, 64]
# branches ['55->56', '55->58', '59->60', '59->64', '60->61', '60->62', '62->59', '62->63']

import pytest
from ansible.plugins.strategy.linear import StrategyModule
from ansible.errors import AnsibleAssertionError
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from unittest.mock import Mock

@pytest.fixture
def strategy_module():
    tqm_mock = Mock()
    strategy = StrategyModule(tqm=tqm_mock)
    strategy.noop_task = Mock(spec=Task)
    return strategy

def test_replace_with_noop_noop_task_none():
    tqm_mock = Mock()
    strategy = StrategyModule(tqm=tqm_mock)
    strategy.noop_task = None
    with pytest.raises(AnsibleAssertionError, match='strategy.linear.StrategyModule.noop_task is None, need Task()'):
        strategy._replace_with_noop([])

def test_replace_with_noop_with_task(strategy_module):
    task = Mock(spec=Task)
    result = strategy_module._replace_with_noop([task])
    assert result == [strategy_module.noop_task]

def test_replace_with_noop_with_block(strategy_module, mocker):
    block = Mock(spec=Block)
    block._parent = Mock()
    mocker.patch.object(strategy_module, '_create_noop_block_from', return_value='noop_block')
    result = strategy_module._replace_with_noop([block])
    strategy_module._create_noop_block_from.assert_called_once_with(block, block._parent)
    assert result == ['noop_block']
