# file lib/ansible/plugins/strategy/linear.py:74-81
# lines [75, 76, 77, 78, 79, 81]
# branches []

import pytest
from unittest.mock import Mock, MagicMock
from ansible.plugins.strategy.linear import StrategyModule
from ansible.playbook.task import Task

@pytest.fixture
def strategy_module():
    tqm = Mock()
    return StrategyModule(tqm)

def test_prepare_and_create_noop_block_from(strategy_module, mocker):
    original_block = Mock()
    parent = Mock()
    iterator = Mock()
    iterator._play._loader = Mock()

    mock_create_noop_block_from = mocker.patch.object(strategy_module, '_create_noop_block_from', return_value='noop_block')

    result = strategy_module._prepare_and_create_noop_block_from(original_block, parent, iterator)

    assert result == 'noop_block'
    assert isinstance(strategy_module.noop_task, Task)
    assert strategy_module.noop_task.action == 'meta'
    assert strategy_module.noop_task.args['_raw_params'] == 'noop'
    assert strategy_module.noop_task.implicit is True
    assert strategy_module.noop_task._loader == iterator._play._loader

    mock_create_noop_block_from.assert_called_once_with(original_block, parent)
