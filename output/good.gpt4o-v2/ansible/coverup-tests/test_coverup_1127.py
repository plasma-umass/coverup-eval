# file: lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# asked: {"lines": [37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 57], [56, 59]]}
# gained: {"lines": [37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 57], [56, 59]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance():
    module = MagicMock()
    instance = GenericBsdIfconfigNetwork(module)
    return instance

def test_populate_ifconfig_path_none(network_instance):
    network_instance.module.get_bin_path = MagicMock(return_value=None)
    result = network_instance.populate()
    assert result == {}

def test_populate_route_path_none(network_instance):
    network_instance.module.get_bin_path = MagicMock(side_effect=['/sbin/ifconfig', None])
    result = network_instance.populate()
    assert result == {}

def test_populate_full_coverage(network_instance):
    network_instance.module.get_bin_path = MagicMock(side_effect=['/sbin/ifconfig', '/sbin/route'])
    network_instance.get_default_interfaces = MagicMock(return_value=('default_ipv4', 'default_ipv6'))
    network_instance.get_interfaces_info = MagicMock(return_value=({'eth0': {}}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
    network_instance.detect_type_media = MagicMock(return_value={'eth0': {}})
    network_instance.merge_default_interface = MagicMock()

    result = network_instance.populate()

    assert result == {
        'interfaces': ['eth0'],
        'eth0': {},
        'default_ipv4': 'default_ipv4',
        'default_ipv6': 'default_ipv6',
        'all_ipv4_addresses': [],
        'all_ipv6_addresses': []
    }
    network_instance.module.get_bin_path.assert_any_call('ifconfig')
    network_instance.module.get_bin_path.assert_any_call('route')
    network_instance.get_default_interfaces.assert_called_once_with('/sbin/route')
    network_instance.get_interfaces_info.assert_called_once_with('/sbin/ifconfig')
    network_instance.detect_type_media.assert_called_once_with({'eth0': {}})
    network_instance.merge_default_interface.assert_any_call('default_ipv4', {'eth0': {}}, 'ipv4')
    network_instance.merge_default_interface.assert_any_call('default_ipv6', {'eth0': {}}, 'ipv6')
