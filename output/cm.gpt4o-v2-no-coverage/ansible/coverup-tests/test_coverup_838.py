# file: lib/ansible/module_utils/facts/network/darwin.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector, DarwinNetwork
from ansible.module_utils.facts.network.base import NetworkCollector

def test_darwin_network_collector_inheritance():
    assert issubclass(DarwinNetworkCollector, NetworkCollector)
    assert DarwinNetworkCollector._fact_class == DarwinNetwork
    assert DarwinNetworkCollector._platform == 'Darwin'

def test_darwin_network_inheritance():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    assert issubclass(DarwinNetwork, GenericBsdIfconfigNetwork)
    assert DarwinNetwork.platform == 'Darwin'
