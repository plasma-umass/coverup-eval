# file: lib/ansible/module_utils/facts/network/generic_bsd.py:156-170
# asked: {"lines": [157, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170], "branches": [[160, 161], [160, 162], [164, 165], [164, 168]]}
# gained: {"lines": [157, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170], "branches": [[160, 161], [160, 162], [164, 165], [164, 168]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance():
    return GenericBsdIfconfigNetwork(module=None)

def test_parse_interface_line_with_loopback(network_instance):
    words = ["lo0:", "flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>", "metric", "0", "mtu", "16384"]
    result = network_instance.parse_interface_line(words)
    assert result['device'] == "lo0"
    assert result['type'] == "loopback"
    assert result['flags'] == ["UP", "LOOPBACK", "RUNNING", "MULTICAST"]
    assert result['macaddress'] == "unknown"
    assert result['metric'] == "0"
    assert result['mtu'] == "16384"

def test_parse_interface_line_without_loopback(network_instance):
    words = ["em0:", "flags=8863<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>", "metric", "0", "mtu", "1500"]
    result = network_instance.parse_interface_line(words)
    assert result['device'] == "em0"
    assert result['type'] == "unknown"
    assert result['flags'] == ["UP", "BROADCAST", "RUNNING", "SIMPLEX", "MULTICAST"]
    assert result['macaddress'] == "unknown"
    assert result['metric'] == "0"
    assert result['mtu'] == "1500"

def test_parse_interface_line_older_freebsd(network_instance):
    words = ["em0:", "flags=8863<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>", "mtu", "1500"]
    result = network_instance.parse_interface_line(words)
    assert result['device'] == "em0"
    assert result['type'] == "unknown"
    assert result['flags'] == ["UP", "BROADCAST", "RUNNING", "SIMPLEX", "MULTICAST"]
    assert result['macaddress'] == "unknown"
    assert result['mtu'] == "1500"
