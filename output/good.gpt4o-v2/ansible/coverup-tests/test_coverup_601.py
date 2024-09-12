# file: lib/ansible/plugins/strategy/linear.py:74-81
# asked: {"lines": [74, 75, 76, 77, 78, 79, 81], "branches": []}
# gained: {"lines": [74, 75, 76, 77, 78, 79, 81], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task import Task
from ansible.playbook.block import Block
from ansible.plugins.strategy.linear import StrategyModule

@pytest.fixture
def strategy_module():
    tqm = MagicMock()
    return StrategyModule(tqm)

def test_prepare_and_create_noop_block_from(strategy_module, mocker):
    original_block = MagicMock()
    parent = MagicMock()
    iterator = MagicMock()
    loader = MagicMock()
    iterator._play._loader = loader

    mocker.patch.object(strategy_module, '_create_noop_block_from', return_value='noop_block')
    mocker.patch.object(Task, 'set_loader', autospec=True)

    result = strategy_module._prepare_and_create_noop_block_from(original_block, parent, iterator)

    assert result == 'noop_block'
    assert isinstance(strategy_module.noop_task, Task)
    assert strategy_module.noop_task.action == 'meta'
    assert strategy_module.noop_task.args['_raw_params'] == 'noop'
    assert strategy_module.noop_task.implicit is True
    Task.set_loader.assert_called_once_with(strategy_module.noop_task, loader)
    strategy_module._create_noop_block_from.assert_called_once_with(original_block, parent)
