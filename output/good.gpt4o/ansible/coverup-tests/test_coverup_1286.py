# file lib/ansible/plugins/strategy/free.py:58-65
# lines [64, 65]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming StrategyBase is defined somewhere in the ansible.plugins.strategy.free module
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def strategy_module():
    tqm_mock = MagicMock()
    module = StrategyModule(tqm=tqm_mock)
    module._flushed_hosts = {}
    return module

def test_filter_notified_hosts(strategy_module):
    # Setup
    notified_hosts = ['host1', 'host2', 'host3']
    strategy_module._flushed_hosts = {
        'host1': True,
        'host2': False,
        'host3': True
    }

    # Execute
    result = strategy_module._filter_notified_hosts(notified_hosts)

    # Verify
    assert result == ['host1', 'host3']

    # Cleanup
    strategy_module._flushed_hosts.clear()
