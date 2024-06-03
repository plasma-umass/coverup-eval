# file lib/ansible/module_utils/facts/network/sunos.py:114-116
# lines [114, 115, 116]
# branches []

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_sunos_network_collector():
    # Ensure the class is a subclass of NetworkCollector
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    
    # Ensure the _fact_class attribute is set correctly
    assert SunOSNetworkCollector._fact_class.__name__ == 'SunOSNetwork'
    
    # Ensure the _platform attribute is set correctly
    assert SunOSNetworkCollector._platform == 'SunOS'
