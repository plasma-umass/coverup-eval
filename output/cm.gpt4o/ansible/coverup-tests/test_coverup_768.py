# file lib/ansible/module_utils/facts/network/aix.py:143-145
# lines [143, 144, 145]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_aix_network_collector():
    # Verify that AIXNetworkCollector is a subclass of NetworkCollector
    assert issubclass(AIXNetworkCollector, NetworkCollector)
    
    # Verify the _fact_class attribute
    assert hasattr(AIXNetworkCollector, '_fact_class')
    assert AIXNetworkCollector._fact_class.__name__ == 'AIXNetwork'
    
    # Verify the _platform attribute
    assert hasattr(AIXNetworkCollector, '_platform')
    assert AIXNetworkCollector._platform == 'AIX'
