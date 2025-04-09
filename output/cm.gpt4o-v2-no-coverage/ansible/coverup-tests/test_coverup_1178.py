# file: lib/ansible/plugins/strategy/linear.py:74-81
# asked: {"lines": [75, 76, 77, 78, 79, 81], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79, 81], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.strategy.linear import StrategyModule
from ansible.playbook.task import Task
from ansible.playbook.block import Block

@pytest.fixture
def strategy_module():
    tqm = MagicMock()
    return StrategyModule(tqm)

@patch.object(Task, 'set_loader')
def test_prepare_and_create_noop_block_from(mock_set_loader, strategy_module):
    original_block = MagicMock()
    parent = MagicMock()
    iterator = MagicMock()
    iterator._play._loader = MagicMock()

    noop_block = strategy_module._prepare_and_create_noop_block_from(original_block, parent, iterator)

    assert isinstance(strategy_module.noop_task, Task)
    assert strategy_module.noop_task.action == 'meta'
    assert strategy_module.noop_task.args['_raw_params'] == 'noop'
    assert strategy_module.noop_task.implicit is True
    mock_set_loader.assert_called_once_with(iterator._play._loader)
    assert isinstance(noop_block, Block)
