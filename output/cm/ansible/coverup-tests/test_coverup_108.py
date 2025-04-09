# file lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# lines [36, 37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64]
# branches ['40->41', '40->43', '45->46', '45->48', '56->57', '56->59']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path = mocker.MagicMock(side_effect=lambda x: '/usr/sbin/' + x)
    return mock_module

@pytest.fixture
def generic_bsd_ifconfig_network(mock_module):
    return GenericBsdIfconfigNetwork(module=mock_module)

def test_populate_with_no_paths(mock_module, generic_bsd_ifconfig_network):
    mock_module.get_bin_path.side_effect = lambda x: None

    result = generic_bsd_ifconfig_network.populate()
    assert result == {}

def test_populate_with_missing_route_path(mock_module, generic_bsd_ifconfig_network):
    mock_module.get_bin_path.side_effect = lambda x: '/usr/sbin/ifconfig' if x == 'ifconfig' else None

    result = generic_bsd_ifconfig_network.populate()
    assert result == {}

def test_populate_with_all_paths(mock_module, generic_bsd_ifconfig_network, mocker):
    mocker.patch.object(generic_bsd_ifconfig_network, 'get_default_interfaces', return_value=({}, {}))
    mocker.patch.object(generic_bsd_ifconfig_network, 'get_interfaces_info', return_value=({}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
    mocker.patch.object(generic_bsd_ifconfig_network, 'detect_type_media', return_value={})
    mocker.patch.object(generic_bsd_ifconfig_network, 'merge_default_interface')

    result = generic_bsd_ifconfig_network.populate()
    assert 'interfaces' in result
    assert 'default_ipv4' in result
    assert 'default_ipv6' in result
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result
