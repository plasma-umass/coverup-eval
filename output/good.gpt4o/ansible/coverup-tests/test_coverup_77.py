# file lib/ansible/module_utils/facts/network/generic_bsd.py:290-310
# lines [290, 291, 292, 293, 294, 295, 297, 298, 299, 301, 302, 303, 305, 306, 308, 309, 310]
# branches ['291->292', '291->293', '293->294', '293->295', '297->298', '297->301', '298->297', '298->299', '302->303', '302->305', '305->306', '305->308', '308->exit', '308->309', '309->exit', '309->310']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

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
                {'address': 'fe80::1', 'prefixlen': 64}
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
    assert 'ipv4' not in defaults
    assert 'ipv6' not in defaults

def test_merge_default_interface_no_interface(network):
    defaults = {
        'address': '192.168.1.1'
    }
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1', 'netmask': '255.255.255.0'}
            ],
            'ipv6': [
                {'address': 'fe80::1', 'prefixlen': 64}
            ],
            'mtu': 1500,
            'macaddress': '00:11:22:33:44:55'
        }
    }
    ip_type = 'ipv4'

    network.merge_default_interface(defaults, interfaces, ip_type)

    assert 'mtu' not in defaults
    assert 'macaddress' not in defaults

def test_merge_default_interface_no_matching_interface(network):
    defaults = {
        'interface': 'eth1',
        'address': '192.168.1.1'
    }
    interfaces = {
        'eth0': {
            'ipv4': [
                {'address': '192.168.1.1', 'netmask': '255.255.255.0'}
            ],
            'ipv6': [
                {'address': 'fe80::1', 'prefixlen': 64}
            ],
            'mtu': 1500,
            'macaddress': '00:11:22:33:44:55'
        }
    }
    ip_type = 'ipv4'

    network.merge_default_interface(defaults, interfaces, ip_type)

    assert 'mtu' not in defaults
    assert 'macaddress' not in defaults
