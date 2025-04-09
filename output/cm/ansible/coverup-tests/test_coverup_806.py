# file lib/ansible/module_utils/facts/network/aix.py:143-145
# lines [143, 144, 145]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetworkCollector

# Since the class is very simple and doesn't have any methods to test directly,
# we will create a test that simply instantiates the class and checks its attributes.

def test_aix_network_collector_instantiation():
    collector = AIXNetworkCollector()
    assert collector._fact_class.__name__ == "AIXNetwork"
    assert collector._platform == "AIX"
