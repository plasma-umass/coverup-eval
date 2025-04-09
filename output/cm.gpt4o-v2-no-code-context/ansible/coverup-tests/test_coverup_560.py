# file: lib/ansible/module_utils/facts/network/aix.py:135-140
# asked: {"lines": [135, 136, 137, 138, 139, 140], "branches": []}
# gained: {"lines": [135, 136, 137, 138, 139, 140], "branches": []}

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork

class MockModule:
    pass

@pytest.fixture
def aix_network():
    module = MockModule()
    return AIXNetwork(module)

def test_parse_interface_line(aix_network):
    words = ['en0:', 'flags=4b<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>']
    result = aix_network.parse_interface_line(words)
    
    assert result['device'] == 'en0'
    assert result['ipv4'] == []
    assert result['ipv6'] == []
    assert result['type'] == 'unknown'
    assert result['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'PROMISC', 'MULTICAST']
    assert result['macaddress'] == 'unknown'
