# file lib/ansible/module_utils/facts/network/hurd.py:85-87
# lines [85, 86, 87]
# branches []

import pytest
from ansible.module_utils.facts.network.hurd import HurdNetworkCollector, HurdPfinetNetwork
from ansible.module_utils.facts.network.base import NetworkCollector

def test_hurd_network_collector():
    # Ensure the class is correctly inheriting from NetworkCollector
    assert issubclass(HurdNetworkCollector, NetworkCollector)
    
    # Ensure the _platform attribute is set correctly
    assert HurdNetworkCollector._platform == 'GNU'
    
    # Ensure the _fact_class attribute is set correctly
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork
