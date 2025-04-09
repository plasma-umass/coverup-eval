# file: lib/ansible/module_utils/facts/network/sunos.py:88-102
# asked: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102], "branches": [[90, 91], [90, 93], [96, 97], [96, 98], [98, 99], [98, 100]]}
# gained: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102], "branches": [[90, 91], [90, 93], [96, 97], [96, 98], [98, 99], [98, 100]]}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork

class MockGenericBsdIfconfigNetwork:
    def get_options(self, option_string):
        return option_string.split(',')

class MockModule:
    pass

@pytest.fixture
def sunos_network(monkeypatch):
    monkeypatch.setattr(SunOSNetwork, 'get_options', MockGenericBsdIfconfigNetwork().get_options)
    return SunOSNetwork(MockModule())

def test_parse_interface_line_new_interface(sunos_network):
    words = ['eth0:', 'UP,BROADCAST,RUNNING', '1500', 'Ethernet']
    current_if = {}
    interfaces = {}
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert result['device'] == 'eth0'
    assert result['ipv4'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING'], 'mtu': 'Ethernet'}]
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_existing_interface(sunos_network):
    words = ['eth0:', 'UP,BROADCAST,RUNNING', '1500', 'Ethernet']
    current_if = {}
    interfaces = {'eth0': {'device': 'eth0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}}
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert result['device'] == 'eth0'
    assert result['ipv4'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING'], 'mtu': 'Ethernet'}]
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_ipv6(sunos_network):
    words = ['eth0:', 'UP,BROADCAST,RUNNING,IPv6', '1500', 'Ethernet']
    current_if = {}
    interfaces = {}
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert result['device'] == 'eth0'
    assert result['ipv6'] == [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'IPv6'], 'mtu': 'Ethernet'}]
    assert result['type'] == 'unknown'
    assert result['macaddress'] == 'unknown'

def test_parse_interface_line_loopback(sunos_network):
    words = ['lo0:', 'UP,LOOPBACK,RUNNING', '1500', 'Local Loopback']
    current_if = {}
    interfaces = {}
    result = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert result['device'] == 'lo0'
    assert result['ipv4'] == [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': 'Local Loopback'}]
    assert result['type'] == 'loopback'
    assert result['macaddress'] == 'unknown'
