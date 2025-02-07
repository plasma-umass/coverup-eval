# file: lib/ansible/module_utils/facts/network/hpux.py:80-82
# asked: {"lines": [80, 81, 82], "branches": []}
# gained: {"lines": [80, 81, 82], "branches": []}

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector, HPUXNetwork

def test_hpux_network_collector_initialization():
    collector = HPUXNetworkCollector()
    assert collector._fact_class == HPUXNetwork
    assert collector._platform == 'HP-UX'
