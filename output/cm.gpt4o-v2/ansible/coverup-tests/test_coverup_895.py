# file: lib/ansible/plugins/strategy/free.py:53-56
# asked: {"lines": [53, 56], "branches": []}
# gained: {"lines": [53, 56], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.free import StrategyModule
from ansible.plugins.strategy import StrategyBase

class MockIterator:
    def is_failed(self, host):
        return host in ['host1', 'host3']

@pytest.fixture
def strategy_module():
    tqm = Mock()
    return StrategyModule(tqm)

def test_filter_notified_failed_hosts(strategy_module):
    iterator = MockIterator()
    notified_hosts = ['host1', 'host2', 'host3', 'host4']
    
    result = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    
    assert result == ['host1', 'host3']
