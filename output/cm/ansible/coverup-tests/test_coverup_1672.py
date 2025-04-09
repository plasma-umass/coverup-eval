# file lib/ansible/plugins/strategy/debug.py:34-37
# lines [34, 35, 36, 37]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.strategy.debug import StrategyModule

# Mocking the TaskQueueManager for testing purposes
@pytest.fixture
def mock_tqm():
    mock_tqm = MagicMock()
    mock_tqm._workers = MagicMock()
    return mock_tqm

# Test function to check if the debugger_active attribute is set to True
def test_strategy_module_debugger_active(mock_tqm):
    strategy_module = StrategyModule(mock_tqm)
    assert strategy_module.debugger_active == True
