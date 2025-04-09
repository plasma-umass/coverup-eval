# file: lib/ansible/module_utils/facts/network/sunos.py:114-116
# asked: {"lines": [114, 115, 116], "branches": []}
# gained: {"lines": [114, 115, 116], "branches": []}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector, SunOSNetwork
from ansible.module_utils.facts.network.base import NetworkCollector

def test_sunos_network_collector_inheritance():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

def test_sunos_network_inheritance():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    assert issubclass(SunOSNetwork, GenericBsdIfconfigNetwork)
    assert SunOSNetwork.platform == 'SunOS'
