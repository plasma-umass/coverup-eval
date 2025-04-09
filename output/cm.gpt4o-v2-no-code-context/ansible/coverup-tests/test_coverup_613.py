# file: lib/ansible/module_utils/facts/network/linux.py:319-322
# asked: {"lines": [319, 320, 321, 322], "branches": []}
# gained: {"lines": [319, 320, 321, 322], "branches": []}

import pytest
from ansible.module_utils.facts.network.linux import LinuxNetworkCollector

def test_linux_network_collector_class_attributes():
    assert LinuxNetworkCollector._platform == 'Linux'
    assert LinuxNetworkCollector._fact_class.__name__ == 'LinuxNetwork'
    assert LinuxNetworkCollector.required_facts == {'distribution', 'platform'}
