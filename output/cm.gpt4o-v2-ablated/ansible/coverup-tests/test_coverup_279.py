# file: lib/ansible/module_utils/facts/network/linux.py:319-322
# asked: {"lines": [319, 320, 321, 322], "branches": []}
# gained: {"lines": [319, 320, 321, 322], "branches": []}

import pytest
from ansible.module_utils.facts.network.linux import LinuxNetworkCollector, NetworkCollector, LinuxNetwork

def test_linux_network_collector_inheritance():
    collector = LinuxNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._platform == 'Linux'
    assert collector._fact_class == LinuxNetwork
    assert collector.required_facts == set(['distribution', 'platform'])

def test_linux_network_collector_required_facts():
    collector = LinuxNetworkCollector()
    assert 'distribution' in collector.required_facts
    assert 'platform' in collector.required_facts
