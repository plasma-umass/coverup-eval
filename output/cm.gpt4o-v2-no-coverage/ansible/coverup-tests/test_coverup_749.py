# file: lib/ansible/module_utils/facts/network/linux.py:319-322
# asked: {"lines": [319, 320, 321, 322], "branches": []}
# gained: {"lines": [319, 320, 321, 322], "branches": []}

import pytest
from ansible.module_utils.facts.network.linux import LinuxNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_linux_network_collector_inheritance():
    assert issubclass(LinuxNetworkCollector, NetworkCollector)

def test_linux_network_collector_attributes():
    collector = LinuxNetworkCollector()
    assert collector._platform == 'Linux'
    assert collector._fact_class.__name__ == 'LinuxNetwork'
    assert collector.required_facts == {'distribution', 'platform'}
