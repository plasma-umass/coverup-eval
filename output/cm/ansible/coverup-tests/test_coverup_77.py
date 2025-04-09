# file lib/ansible/module_utils/facts/network/generic_bsd.py:290-310
# lines [290, 291, 292, 293, 294, 295, 297, 298, 299, 301, 302, 303, 305, 306, 308, 309, 310]
# branches ['291->292', '291->293', '293->294', '293->295', '297->298', '297->301', '298->297', '298->299', '302->303', '302->305', '305->306', '305->308', '308->exit', '308->309', '309->exit', '309->310']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_interfaces():
    return {
        'em0': {
            'device': 'em0',
            'ipv4': [{'address': '192.168.1.100', 'netmask': '255.255.255.0'}],
            'ipv6': [{'address': 'fe80::1', 'prefix': '64'}],
            'macaddress': 'aa:bb:cc:dd:ee:ff'
        },
        'em1': {
            'device': 'em1',
            'ipv4': [{'address': '192.168.2.100', 'netmask': '255.255.255.0'}],
            'ipv6': [{'address': 'fe80::2', 'prefix': '64'}],
            'macaddress': 'ff:ee:dd:cc:bb:aa'
        }
    }

@pytest.fixture
def mock_module():
    return MagicMock()

def test_merge_default_interface_with_address(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    defaults = {'interface': 'em0', 'address': '192.168.1.100'}
    network.merge_default_interface(defaults, mock_interfaces, 'ipv4')
    assert defaults['netmask'] == '255.255.255.0'
    assert defaults['macaddress'] == 'aa:bb:cc:dd:ee:ff'

def test_merge_default_interface_without_address(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    defaults = {'interface': 'em0'}
    network.merge_default_interface(defaults, mock_interfaces, 'ipv4')
    assert defaults['netmask'] == '255.255.255.0'
    assert defaults['macaddress'] == 'aa:bb:cc:dd:ee:ff'

def test_merge_default_interface_with_nonexistent_address(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    defaults = {'interface': 'em0', 'address': '10.0.0.1'}
    network.merge_default_interface(defaults, mock_interfaces, 'ipv4')
    assert defaults['netmask'] == '255.255.255.0'
    assert defaults['macaddress'] == 'aa:bb:cc:dd:ee:ff'

def test_merge_default_interface_with_nonexistent_interface(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    defaults = {'interface': 'em2'}
    network.merge_default_interface(defaults, mock_interfaces, 'ipv4')
    assert 'netmask' not in defaults
    assert 'macaddress' not in defaults

def test_merge_default_interface_with_no_interface_key(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    defaults = {}
    network.merge_default_interface(defaults, mock_interfaces, 'ipv4')
    assert 'interface' not in defaults
    assert 'netmask' not in defaults
    assert 'macaddress' not in defaults
