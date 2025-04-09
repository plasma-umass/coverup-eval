# file: lib/ansible/module_utils/facts/network/sunos.py:88-102
# asked: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102], "branches": [[90, 91], [90, 93], [96, 97], [96, 98], [98, 99], [98, 100]]}
# gained: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102], "branches": [[90, 91], [90, 93], [96, 97], [96, 98], [98, 99], [98, 100]]}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork
from unittest.mock import Mock

@pytest.fixture
def sunos_network():
    module = Mock()
    return SunOSNetwork(module)

def test_parse_interface_line_new_interface(sunos_network):
    words = ['eth0:', 'flags=100863<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500']
    current_if = None
    interfaces = {}
    
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result['device'] == 'eth0'
    assert result['ipv4'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST'], 'mtu': '1500'}]
    assert result['ipv6'] == []
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_existing_interface(sunos_network):
    words = ['eth0:', 'flags=100863<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500']
    current_if = None
    interfaces = {
        'eth0': {
            'device': 'eth0',
            'ipv4': [],
            'ipv6': [],
            'type': 'unknown'
        }
    }
    
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result['device'] == 'eth0'
    assert result['ipv4'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST'], 'mtu': '1500'}]
    assert result['ipv6'] == []
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_ipv6(sunos_network):
    words = ['eth0:', 'flags=100863<UP,BROADCAST,RUNNING,MULTICAST,IPv6>', 'mtu', '1500']
    current_if = None
    interfaces = {}
    
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result['device'] == 'eth0'
    assert result['ipv4'] == []
    assert result['ipv6'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST', 'IPv6'], 'mtu': '1500'}]
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_loopback(sunos_network):
    words = ['lo0:', 'flags=100863<UP,LOOPBACK,RUNNING>', 'mtu', '8232']
    current_if = None
    interfaces = {}
    
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result['device'] == 'lo0'
    assert result['ipv4'] == [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': '8232'}]
    assert result['ipv6'] == []
    assert result['type'] == 'loopback'
    assert result['macaddress'] == 'unknown'
