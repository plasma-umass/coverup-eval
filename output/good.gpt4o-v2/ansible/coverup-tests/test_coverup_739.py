# file: lib/ansible/plugins/strategy/host_pinned.py:41-45
# asked: {"lines": [41, 43, 44, 45], "branches": []}
# gained: {"lines": [41, 43, 44, 45], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.host_pinned import StrategyModule
from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule

@pytest.fixture
def mock_tqm():
    tqm = Mock()
    tqm.get_inventory.return_value = Mock()
    return tqm

def test_strategy_module_init(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned is True

def test_free_strategy_module_init(mock_tqm):
    strategy = FreeStrategyModule(mock_tqm)
    assert strategy._host_pinned is False
