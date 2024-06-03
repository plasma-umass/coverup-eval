# file lib/ansible/plugins/strategy/debug.py:34-37
# lines [34, 35, 36, 37]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the StrategyModule is defined in ansible.plugins.strategy.debug
from ansible.plugins.strategy.debug import StrategyModule

@pytest.fixture
def mock_tqm():
    return Mock()

def test_strategy_module_initialization(mock_tqm):
    strategy_module = StrategyModule(mock_tqm)
    assert strategy_module.debugger_active is True
