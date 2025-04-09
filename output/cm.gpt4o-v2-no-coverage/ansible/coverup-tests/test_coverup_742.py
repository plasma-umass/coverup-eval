# file: lib/ansible/plugins/strategy/debug.py:34-37
# asked: {"lines": [34, 35, 36, 37], "branches": []}
# gained: {"lines": [34, 35, 36, 37], "branches": []}

import pytest
from ansible.plugins.strategy.debug import StrategyModule
from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule

class MockTQM:
    def get_inventory(self):
        return "mock_inventory"

    def _workers(self):
        return "mock_workers"

    def get_variable_manager(self):
        return "mock_variable_manager"

    def get_loader(self):
        return "mock_loader"

    def _final_q(self):
        return "mock_final_q"

@pytest.fixture
def mock_tqm():
    return MockTQM()

def test_strategy_module_init(mock_tqm):
    strategy = StrategyModule(mock_tqm)
    assert strategy.debugger_active == True
    assert isinstance(strategy, LinearStrategyModule)
