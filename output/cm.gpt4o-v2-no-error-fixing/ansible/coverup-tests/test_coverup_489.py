# file: lib/ansible/plugins/strategy/free.py:58-65
# asked: {"lines": [58, 64, 65], "branches": []}
# gained: {"lines": [58, 64, 65], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.strategy.free import StrategyModule
from ansible.plugins.strategy import StrategyBase

@pytest.fixture
def strategy_module():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    strategy._flushed_hosts = {
        'host1': True,
        'host2': False,
        'host3': True
    }
    return strategy

def test_filter_notified_hosts(strategy_module):
    notified_hosts = ['host1', 'host2', 'host3', 'host4']
    filtered_hosts = strategy_module._filter_notified_hosts(notified_hosts)
    assert filtered_hosts == ['host1', 'host3']
