# file: lib/ansible/module_utils/facts/network/hpux.py:80-82
# asked: {"lines": [80, 81, 82], "branches": []}
# gained: {"lines": [80, 81, 82], "branches": []}

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_hpux_network_collector_inheritance():
    collector = HPUXNetworkCollector()
    assert isinstance(collector, NetworkCollector)

def test_hpux_network_collector_fact_class():
    assert HPUXNetworkCollector._fact_class.__name__ == 'HPUXNetwork'

def test_hpux_network_collector_platform():
    assert HPUXNetworkCollector._platform == 'HP-UX'
