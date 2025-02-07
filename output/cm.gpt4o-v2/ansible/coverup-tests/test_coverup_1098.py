# file: lib/ansible/module_utils/facts/network/generic_bsd.py:290-310
# asked: {"lines": [291, 292, 293, 294, 295, 297, 298, 299, 301, 302, 303, 305, 306, 308, 309, 310], "branches": [[291, 292], [291, 293], [293, 294], [293, 295], [297, 298], [297, 301], [298, 297], [298, 299], [302, 303], [302, 305], [305, 306], [305, 308], [308, 0], [308, 309], [309, 0], [309, 310]]}
# gained: {"lines": [291, 292, 293, 294, 295, 297, 298, 299, 301, 302, 303, 305, 306, 308, 309, 310], "branches": [[291, 292], [291, 293], [293, 294], [293, 295], [297, 298], [297, 301], [298, 297], [298, 299], [302, 303], [302, 305], [305, 306], [305, 308], [308, 0], [308, 309], [309, 0], [309, 310]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import MagicMock

@pytest.fixture
def network():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module)

def test_merge_default_interface_no_interface_in_defaults(network):
    defaults = {}
    interfaces = {'eth0': {'ipv4': [], 'ipv6': []}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {}

def test_merge_default_interface_interface_not_in_interfaces(network):
    defaults = {'interface': 'eth1'}
    interfaces = {'eth0': {'ipv4': [], 'ipv6': []}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface': 'eth1'}

def test_merge_default_interface_copy_values(network):
    defaults = {'interface': 'eth0'}
    interfaces = {'eth0': {'ipv4': [], 'ipv6': [], 'mtu': 1500}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface': 'eth0', 'mtu': 1500}

def test_merge_default_interface_with_address(network):
    defaults = {'interface': 'eth0', 'address': '192.168.1.1'}
    interfaces = {'eth0': {'ipv4': [{'address': '192.168.1.1', 'netmask': '255.255.255.0'}], 'ipv6': []}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface': 'eth0', 'address': '192.168.1.1', 'netmask': '255.255.255.0'}

def test_merge_default_interface_without_address(network):
    defaults = {'interface': 'eth0'}
    interfaces = {'eth0': {'ipv4': [{'address': '192.168.1.1', 'netmask': '255.255.255.0'}], 'ipv6': []}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface': 'eth0', 'address': '192.168.1.1', 'netmask': '255.255.255.0'}
