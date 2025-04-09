# file: lib/ansible/module_utils/facts/network/aix.py:143-145
# asked: {"lines": [143, 144, 145], "branches": []}
# gained: {"lines": [143, 144, 145], "branches": []}

import pytest
from ansible.module_utils.facts.network.aix import AIXNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_aix_network_collector_inheritance():
    collector = AIXNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._platform == 'AIX'
    assert collector._fact_class.__name__ == 'AIXNetwork'
