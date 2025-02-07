# file: lib/ansible/module_utils/facts/network/aix.py:135-140
# asked: {"lines": [135, 136, 137, 138, 139, 140], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139, 140], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def aix_network():
    module = MagicMock()
    return AIXNetwork(module)

def test_parse_interface_line(aix_network):
    words = ["en0:", "flags=4b<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST>"]
    result = aix_network.parse_interface_line(words)
    
    assert result['device'] == "en0"
    assert result['ipv4'] == []
    assert result['ipv6'] == []
    assert result['type'] == 'unknown'
    assert result['flags'] == aix_network.get_options("flags=4b<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST>")
    assert result['macaddress'] == 'unknown'
