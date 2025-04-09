# file: lib/ansible/module_utils/facts/network/darwin.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
from ansible.module_utils.facts.network.darwin import DarwinNetwork
from ansible.module_utils.facts.network.base import NetworkCollector

def test_darwin_network_collector_inheritance():
    collector = DarwinNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._fact_class == DarwinNetwork
    assert collector._platform == 'Darwin'
