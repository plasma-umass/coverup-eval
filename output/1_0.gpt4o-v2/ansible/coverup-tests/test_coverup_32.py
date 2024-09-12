# file: lib/ansible/module_utils/facts/network/base.py:43-70
# asked: {"lines": [43, 45, 46, 47, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 66, 68, 70], "branches": [[62, 63], [62, 66]]}
# gained: {"lines": [43, 45, 46, 47, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 66, 68, 70], "branches": [[62, 63], [62, 66]]}

import pytest
from ansible.module_utils.facts.network.base import NetworkCollector, Network

class MockModule:
    pass

class MockNetwork(Network):
    def __init__(self, module, load_on_init=False):
        super().__init__(module, load_on_init)
    
    def populate(self, collected_facts=None):
        if collected_facts is None:
            collected_facts = {}
        collected_facts.update({
            'interfaces': ['eth0', 'eth1'],
            'default_ipv4': '192.168.1.1',
            'default_ipv6': 'fe80::1',
            'all_ipv4_addresses': ['192.168.1.1', '192.168.1.2'],
            'all_ipv6_addresses': ['fe80::1', 'fe80::2']
        })
        return collected_facts

@pytest.fixture
def mock_network(monkeypatch):
    monkeypatch.setattr(NetworkCollector, '_fact_class', MockNetwork)

def test_collect_with_module(mock_network):
    module = MockModule()
    collector = NetworkCollector()
    collected_facts = collector.collect(module=module)
    
    assert 'interfaces' in collected_facts
    assert 'default_ipv4' in collected_facts
    assert 'default_ipv6' in collected_facts
    assert 'all_ipv4_addresses' in collected_facts
    assert 'all_ipv6_addresses' in collected_facts

def test_collect_without_module(mock_network):
    collector = NetworkCollector()
    collected_facts = collector.collect(module=None)
    
    assert collected_facts == {}
