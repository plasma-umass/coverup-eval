# file lib/ansible/module_utils/facts/network/hpux.py:80-82
# lines [80, 81, 82]
# branches []

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector, NetworkCollector, HPUXNetwork

def test_hpux_network_collector():
    # Verify that HPUXNetworkCollector is a subclass of NetworkCollector
    assert issubclass(HPUXNetworkCollector, NetworkCollector)
    
    # Verify that the _fact_class attribute is set correctly
    assert HPUXNetworkCollector._fact_class is HPUXNetwork
    
    # Verify that the _platform attribute is set correctly
    assert HPUXNetworkCollector._platform == 'HP-UX'
