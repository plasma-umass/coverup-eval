# file: lib/ansible/plugins/strategy/free.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import pytest
from ansible.plugins.strategy.free import StrategyModule

class MockTQM:
    def get_inventory(self):
        return "mock_inventory"

    def get_variable_manager(self):
        return "mock_variable_manager"

    def get_loader(self):
        return "mock_loader"

    _workers = "mock_workers"
    _final_q = "mock_final_q"

@pytest.fixture
def mock_tqm():
    return MockTQM()

def test_strategy_module_init(mock_tqm):
    strategy_module = StrategyModule(mock_tqm)
    assert strategy_module._tqm == mock_tqm
    assert strategy_module._inventory == "mock_inventory"
    assert strategy_module._workers == "mock_workers"
    assert strategy_module._variable_manager == "mock_variable_manager"
    assert strategy_module._loader == "mock_loader"
    assert strategy_module._final_q == "mock_final_q"
    assert strategy_module._host_pinned == False
