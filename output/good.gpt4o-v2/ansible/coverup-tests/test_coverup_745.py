# file: lib/ansible/plugins/strategy/free.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def mock_tqm():
    return Mock()

def test_strategy_module_init(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned == False
    assert strategy._tqm == mock_tqm
    assert hasattr(strategy, '_inventory')
    assert hasattr(strategy, '_workers')
    assert hasattr(strategy, '_variable_manager')
    assert hasattr(strategy, '_loader')
    assert hasattr(strategy, '_final_q')
    assert hasattr(strategy, '_step')
    assert hasattr(strategy, '_diff')
    assert hasattr(strategy, '_queued_task_cache')
    assert hasattr(strategy, '_display')
    assert hasattr(strategy, '_pending_results')
    assert hasattr(strategy, '_pending_handler_results')
    assert hasattr(strategy, '_cur_worker')
    assert hasattr(strategy, '_blocked_hosts')
    assert hasattr(strategy, '_flushed_hosts')
    assert hasattr(strategy, '_results')
    assert hasattr(strategy, '_handler_results')
    assert hasattr(strategy, '_results_lock')
    assert hasattr(strategy, '_results_thread')
    assert hasattr(strategy, '_active_connections')
    assert hasattr(strategy, '_hosts_cache')
    assert hasattr(strategy, '_hosts_cache_all')
    assert hasattr(strategy, 'debugger_active')
