# file: lib/ansible/plugins/strategy/free.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import pytest
from ansible.plugins.strategy.free import StrategyModule
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def mock_tqm(mocker):
    mock_tqm = mocker.Mock(spec=TaskQueueManager)
    mock_tqm.get_inventory.return_value = mocker.Mock()
    mock_tqm._workers = mocker.Mock()
    mock_tqm.get_variable_manager.return_value = mocker.Mock()
    mock_tqm.get_loader.return_value = mocker.Mock()
    mock_tqm._final_q = mocker.Mock()
    return mock_tqm

def test_strategy_module_init(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned is False
    assert strategy._tqm == mock_tqm
    assert hasattr(strategy, '_inventory')
    assert hasattr(strategy, '_workers')
    assert hasattr(strategy, '_variable_manager')
    assert hasattr(strategy, '_loader')
    assert hasattr(strategy, '_final_q')
