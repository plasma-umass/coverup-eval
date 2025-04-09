# file: lib/ansible/plugins/strategy/host_pinned.py:41-45
# asked: {"lines": [41, 43, 44, 45], "branches": []}
# gained: {"lines": [41, 43, 44, 45], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.strategy.host_pinned import StrategyModule
from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule

@pytest.fixture
def mock_tqm():
    tqm = MagicMock()
    tqm.get_inventory.return_value = MagicMock()
    return tqm

def test_strategy_module_init(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned is True

def test_strategy_module_inheritance(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert isinstance(strategy, FreeStrategyModule)
