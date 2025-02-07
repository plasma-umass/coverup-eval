# file: lib/ansible/module_utils/facts/network/darwin.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_darwin_network_collector_inheritance():
    collector = DarwinNetworkCollector()
    assert isinstance(collector, NetworkCollector)

def test_darwin_network_collector_fact_class():
    assert DarwinNetworkCollector._fact_class.__name__ == 'DarwinNetwork'

def test_darwin_network_collector_platform():
    assert DarwinNetworkCollector._platform == 'Darwin'
