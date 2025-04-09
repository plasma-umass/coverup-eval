# file: lib/ansible/plugins/strategy/free.py:53-56
# asked: {"lines": [53, 56], "branches": []}
# gained: {"lines": [53, 56], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.strategy.free import StrategyModule

@pytest.fixture
def iterator():
    return Mock()

@pytest.fixture
def strategy_module():
    return StrategyModule(Mock())

def test_filter_notified_failed_hosts_all_failed(iterator, strategy_module):
    iterator.is_failed.side_effect = lambda host: True
    notified_hosts = ['host1', 'host2', 'host3']
    result = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    assert result == notified_hosts

def test_filter_notified_failed_hosts_none_failed(iterator, strategy_module):
    iterator.is_failed.side_effect = lambda host: False
    notified_hosts = ['host1', 'host2', 'host3']
    result = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    assert result == []

def test_filter_notified_failed_hosts_some_failed(iterator, strategy_module):
    iterator.is_failed.side_effect = lambda host: host == 'host2'
    notified_hosts = ['host1', 'host2', 'host3']
    result = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    assert result == ['host2']
