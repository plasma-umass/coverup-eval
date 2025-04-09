# file: lib/ansible/module_utils/facts/network/aix.py:143-145
# asked: {"lines": [143, 144, 145], "branches": []}
# gained: {"lines": [143, 144, 145], "branches": []}

import pytest
from ansible.module_utils.facts.network.aix import AIXNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_aix_network_collector_inheritance():
    # Ensure AIXNetworkCollector inherits from NetworkCollector
    assert issubclass(AIXNetworkCollector, NetworkCollector)

def test_aix_network_collector_fact_class():
    # Ensure the _fact_class attribute is set correctly
    assert AIXNetworkCollector._fact_class.__name__ == 'AIXNetwork'

def test_aix_network_collector_platform():
    # Ensure the _platform attribute is set correctly
    assert AIXNetworkCollector._platform == 'AIX'
