# file: lib/ansible/plugins/strategy/debug.py:34-37
# asked: {"lines": [34, 35, 36, 37], "branches": []}
# gained: {"lines": [34, 35, 36, 37], "branches": []}

import pytest
from ansible.plugins.strategy.debug import StrategyModule
from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule

def test_strategy_module_init(mocker):
    # Mock the tqm parameter
    tqm_mock = mocker.Mock()

    # Instantiate the StrategyModule
    strategy_module = StrategyModule(tqm_mock)

    # Assertions to verify the correct initialization
    assert isinstance(strategy_module, LinearStrategyModule)
    assert strategy_module.debugger_active is True
