# file lib/ansible/module_utils/facts/network/linux.py:319-322
# lines [319, 320, 321, 322]
# branches []

import pytest
from ansible.module_utils.facts.network.linux import LinuxNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_linux_network_collector_initialization():
    collector = LinuxNetworkCollector()
    assert collector._platform == 'Linux'
    assert collector._fact_class.__name__ == 'LinuxNetwork'
    assert collector.required_facts == {'distribution', 'platform'}

def test_linux_network_collector_inheritance():
    collector = LinuxNetworkCollector()
    assert isinstance(collector, NetworkCollector)
