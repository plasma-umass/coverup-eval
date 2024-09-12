# file: lib/ansible/module_utils/facts/network/netbsd.py:46-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import pytest
from ansible.module_utils.facts.network.netbsd import NetBSDNetworkCollector, NetBSDNetwork

def test_netbsd_network_collector_initialization():
    collector = NetBSDNetworkCollector()
    assert collector._fact_class == NetBSDNetwork
    assert collector._platform == 'NetBSD'
