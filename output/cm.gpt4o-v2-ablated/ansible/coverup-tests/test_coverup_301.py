# file: lib/ansible/module_utils/facts/network/sunos.py:114-116
# asked: {"lines": [114, 115, 116], "branches": []}
# gained: {"lines": [114, 115, 116], "branches": []}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector, SunOSNetwork
from ansible.module_utils.facts.network.base import NetworkCollector

def test_sunos_network_collector_inheritance():
    collector = SunOSNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'
