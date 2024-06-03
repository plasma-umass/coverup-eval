# file lib/ansible/plugins/strategy/free.py:53-56
# lines [56]
# branches []

import pytest
from unittest.mock import Mock

# Assuming StrategyBase is defined somewhere in ansible.plugins.strategy.free
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def mock_iterator():
    return Mock()

@pytest.fixture
def strategy_module():
    # Mocking the 'tqm' argument required by StrategyModule
    mock_tqm = Mock()
    return StrategyModule(tqm=mock_tqm)

def test_filter_notified_failed_hosts(mock_iterator, strategy_module):
    # Setup
    notified_hosts = ['host1', 'host2', 'host3']
    mock_iterator.is_failed.side_effect = lambda host: host == 'host2'
    
    # Execute
    result = strategy_module._filter_notified_failed_hosts(mock_iterator, notified_hosts)
    
    # Verify
    assert result == ['host2']
    mock_iterator.is_failed.assert_any_call('host1')
    mock_iterator.is_failed.assert_any_call('host2')
    mock_iterator.is_failed.assert_any_call('host3')
    assert mock_iterator.is_failed.call_count == 3
