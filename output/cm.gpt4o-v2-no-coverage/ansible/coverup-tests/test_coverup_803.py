# file: lib/ansible/plugins/strategy/free.py:58-65
# asked: {"lines": [58, 64, 65], "branches": []}
# gained: {"lines": [58, 64, 65], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def strategy_module():
    # Create a mock tqm object
    tqm = MagicMock()
    tqm.get_inventory.return_value = MagicMock()
    tqm._workers = MagicMock()
    tqm.get_variable_manager.return_value = MagicMock()
    tqm.get_loader.return_value = MagicMock()
    tqm._final_q = MagicMock()

    # Instantiate the StrategyModule with the mock tqm
    return StrategyModule(tqm)

def test_filter_notified_hosts(strategy_module):
    # Setup the _flushed_hosts attribute
    strategy_module._flushed_hosts = {
        'host1': True,
        'host2': False,
        'host3': True
    }

    # Define the notified_hosts input
    notified_hosts = ['host1', 'host2', 'host3', 'host4']

    # Call the method
    result = strategy_module._filter_notified_hosts(notified_hosts)

    # Assert the expected output
    assert result == ['host1', 'host3']

    # Clean up
    strategy_module._flushed_hosts.clear()
