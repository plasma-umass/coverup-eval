# file: lib/ansible/plugins/strategy/free.py:58-65
# asked: {"lines": [58, 64, 65], "branches": []}
# gained: {"lines": [58, 64, 65], "branches": []}

import pytest
from ansible.plugins.strategy.free import StrategyModule

class MockTQM:
    def get_inventory(self):
        return None

    def get_variable_manager(self):
        return None

    def get_loader(self):
        return None

    _workers = []
    _final_q = []

@pytest.fixture
def strategy_module():
    tqm = MockTQM()
    strategy = StrategyModule(tqm)
    strategy._flushed_hosts = {}
    return strategy

def test_filter_notified_hosts_empty(strategy_module):
    notified_hosts = []
    result = strategy_module._filter_notified_hosts(notified_hosts)
    assert result == []

def test_filter_notified_hosts_all_flushed(strategy_module):
    notified_hosts = ['host1', 'host2']
    strategy_module._flushed_hosts = {'host1': True, 'host2': True}
    result = strategy_module._filter_notified_hosts(notified_hosts)
    assert result == ['host1', 'host2']

def test_filter_notified_hosts_some_flushed(strategy_module):
    notified_hosts = ['host1', 'host2', 'host3']
    strategy_module._flushed_hosts = {'host1': True, 'host2': False, 'host3': True}
    result = strategy_module._filter_notified_hosts(notified_hosts)
    assert result == ['host1', 'host3']

def test_filter_notified_hosts_none_flushed(strategy_module):
    notified_hosts = ['host1', 'host2']
    strategy_module._flushed_hosts = {'host1': False, 'host2': False}
    result = strategy_module._filter_notified_hosts(notified_hosts)
    assert result == []
