# file: lib/ansible/module_utils/facts/network/freebsd.py:31-33
# asked: {"lines": [31, 32, 33], "branches": []}
# gained: {"lines": [31, 32, 33], "branches": []}

import pytest
from ansible.module_utils.facts.network.freebsd import FreeBSDNetworkCollector, FreeBSDNetwork

def test_freebsd_network_collector_initialization():
    collector = FreeBSDNetworkCollector()
    assert collector._fact_class == FreeBSDNetwork
    assert collector._platform == 'FreeBSD'
