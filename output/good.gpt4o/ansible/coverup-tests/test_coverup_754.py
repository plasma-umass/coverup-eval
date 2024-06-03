# file lib/ansible/module_utils/facts/network/darwin.py:47-49
# lines [47, 48, 49]
# branches []

import pytest
from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_darwin_network_collector():
    # Verify that DarwinNetworkCollector is a subclass of NetworkCollector
    assert issubclass(DarwinNetworkCollector, NetworkCollector)
    
    # Verify that the _fact_class attribute is set correctly
    assert hasattr(DarwinNetworkCollector, '_fact_class')
    assert DarwinNetworkCollector._fact_class.__name__ == 'DarwinNetwork'
    
    # Verify that the _platform attribute is set correctly
    assert hasattr(DarwinNetworkCollector, '_platform')
    assert DarwinNetworkCollector._platform == 'Darwin'
