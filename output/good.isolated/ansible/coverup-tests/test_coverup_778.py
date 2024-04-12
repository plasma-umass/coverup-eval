# file lib/ansible/plugins/strategy/free.py:58-65
# lines [58, 64, 65]
# branches []

import pytest
from ansible.plugins.strategy.free import StrategyModule
from unittest.mock import MagicMock

# Mock classes to avoid side effects
class MockHost:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def strategy_module(mocker):
    # Mock the StrategyBase constructor since we don't need the actual base initialization
    mocker.patch('ansible.plugins.strategy.StrategyBase.__init__', return_value=None)
    
    # Mock TaskQueueManager for StrategyModule
    mock_tqm = MagicMock()
    
    # Create an instance of the StrategyModule with the mocked TaskQueueManager
    strategy_module = StrategyModule(mock_tqm)
    
    # Mock the necessary attributes for the test
    strategy_module._flushed_hosts = {}
    
    return strategy_module

def test_filter_notified_hosts(strategy_module):
    # Setup test hosts
    host1 = MockHost('host1')
    host2 = MockHost('host2')
    host3 = MockHost('host3')
    
    # Setup the _flushed_hosts to simulate the condition
    strategy_module._flushed_hosts = {
        host1: True,
        host2: False,
        host3: True
    }
    
    # List of notified hosts
    notified_hosts = [host1, host2, host3]
    
    # Call the method under test
    filtered_hosts = strategy_module._filter_notified_hosts(notified_hosts)
    
    # Assert the expected hosts are in the filtered list
    assert host1 in filtered_hosts
    assert host2 not in filtered_hosts
    assert host3 in filtered_hosts
    
    # Assert the length of the filtered list is correct
    assert len(filtered_hosts) == 2
