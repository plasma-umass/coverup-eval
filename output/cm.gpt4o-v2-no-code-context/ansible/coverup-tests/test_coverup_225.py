# file: lib/ansible/module_utils/facts/network/generic_bsd.py:156-170
# asked: {"lines": [156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170], "branches": [[160, 161], [160, 162], [164, 165], [164, 168]]}
# gained: {"lines": [156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170], "branches": [[160, 161], [160, 162], [164, 165], [164, 168]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_parse_interface_line_newer_freebsd(network):
    words = ['em0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'metric', '0', 'mtu', '1500']
    result = network.parse_interface_line(words)
    assert result['device'] == 'em0'
    assert result['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'
    assert result['metric'] == '0'
    assert result['mtu'] == '1500'

def test_parse_interface_line_older_freebsd(network):
    words = ['em0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'mtu', '1500']
    result = network.parse_interface_line(words)
    assert result['device'] == 'em0'
    assert result['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'
    assert result['mtu'] == '1500'

def test_parse_interface_line_loopback(network):
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '16384']
    result = network.parse_interface_line(words)
    assert result['device'] == 'lo0'
    assert result['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert result['type'] == 'loopback'
    assert result['macaddress'] == 'unknown'
    assert result['metric'] == '0'
    assert result['mtu'] == '16384'
