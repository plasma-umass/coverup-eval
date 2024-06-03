# file lib/ansible/module_utils/facts/network/generic_bsd.py:290-310
# lines [306]
# branches ['302->305', '305->306', '308->exit']

import pytest
from unittest.mock import MagicMock

# Assuming the class GenericBsdIfconfigNetwork is imported from the module
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network():
    module_mock = MagicMock()
    return GenericBsdIfconfigNetwork(module_mock)

def test_merge_default_interface(network):
    defaults = {
        'interface': 'eth0',
        'address': '192.168.1.1'
    }
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1', 'netmask': '255.255.255.0'},
                {'address': '192.168.1.2', 'netmask': '255.255.255.0'}
            ],
            'ipv6': [
                {'address': 'fe80::1', 'prefixlen': 64},
                {'address': 'fe80::2', 'prefixlen': 64}
            ],
            'mtu': 1500,
            'macaddress': '00:11:22:33:44:55'
        }
    }
    ip_type = 'ipv4'

    network.merge_default_interface(defaults, interfaces, ip_type)

    assert defaults['mtu'] == 1500
    assert defaults['macaddress'] == '00:11:22:33:44:55'
    assert defaults['netmask'] == '255.255.255.0'

def test_merge_default_interface_no_address_match(network):
    defaults = {
        'interface': 'eth0',
        'address': '192.168.1.3'
    }
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1', 'netmask': '255.255.255.0'},
                {'address': '192.168.1.2', 'netmask': '255.255.255.0'}
            ],
            'ipv6': [
                {'address': 'fe80::1', 'prefixlen': 64},
                {'address': 'fe80::2', 'prefixlen': 64}
            ],
            'mtu': 1500,
            'macaddress': '00:11:22:33:44:55'
        }
    }
    ip_type = 'ipv4'

    network.merge_default_interface(defaults, interfaces, ip_type)

    assert defaults['mtu'] == 1500
    assert defaults['macaddress'] == '00:11:22:33:44:55'
    assert defaults['netmask'] == '255.255.255.0'
    assert defaults['address'] == '192.168.1.1'
