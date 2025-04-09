# file: lib/ansible/plugins/strategy/free.py:53-56
# asked: {"lines": [53, 56], "branches": []}
# gained: {"lines": [53, 56], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def strategy_module():
    tqm = Mock()
    return StrategyModule(tqm)

def test_filter_notified_failed_hosts(strategy_module):
    iterator = Mock()
    notified_hosts = ['host1', 'host2', 'host3']
    
    # Mock the is_failed method to return True for 'host2' and False for others
    iterator.is_failed.side_effect = lambda host: host == 'host2'
    
    result = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    
    # Verify that only 'host2' is returned
    assert result == ['host2']
    
    # Verify that is_failed was called for each host
    iterator.is_failed.assert_any_call('host1')
    iterator.is_failed.assert_any_call('host2')
    iterator.is_failed.assert_any_call('host3')
    assert iterator.is_failed.call_count == 3
