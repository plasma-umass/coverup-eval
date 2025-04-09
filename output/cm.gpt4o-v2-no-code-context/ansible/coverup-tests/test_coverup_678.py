# file: lib/ansible/module_utils/facts/network/hpux.py:80-82
# asked: {"lines": [80, 81, 82], "branches": []}
# gained: {"lines": [80, 81, 82], "branches": []}

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector, NetworkCollector, HPUXNetwork

def test_hpux_network_collector_class_attributes():
    assert issubclass(HPUXNetworkCollector, NetworkCollector)
    assert HPUXNetworkCollector._fact_class == HPUXNetwork
    assert HPUXNetworkCollector._platform == 'HP-UX'
