# file: lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# asked: {"lines": [36, 37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 57], [56, 59]]}
# gained: {"lines": [36, 37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 57], [56, 59]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda x: f"/sbin/{x}" if x in ['ifconfig', 'route'] else None
    return module

@pytest.fixture
def network_instance(mock_module):
    return GenericBsdIfconfigNetwork(module=mock_module)

def test_populate_no_ifconfig_path(network_instance, mock_module):
    mock_module.get_bin_path.side_effect = lambda x: None if x == 'ifconfig' else f"/sbin/{x}"
    result = network_instance.populate()
    assert result == {}

def test_populate_no_route_path(network_instance, mock_module):
    mock_module.get_bin_path.side_effect = lambda x: None if x == 'route' else f"/sbin/{x}"
    result = network_instance.populate()
    assert result == {}

@patch.object(GenericBsdIfconfigNetwork, 'get_default_interfaces', return_value=({'interface': 'em0'}, {'interface': 'em1'}))
@patch.object(GenericBsdIfconfigNetwork, 'get_interfaces_info', return_value=({'em0': {'device': 'em0'}, 'em1': {'device': 'em1'}}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
@patch.object(GenericBsdIfconfigNetwork, 'detect_type_media', return_value={'em0': {'device': 'em0', 'type': 'ether'}, 'em1': {'device': 'em1', 'type': 'ether'}})
@patch.object(GenericBsdIfconfigNetwork, 'merge_default_interface')
def test_populate_full_coverage(mock_merge_default_interface, mock_detect_type_media, mock_get_interfaces_info, mock_get_default_interfaces, network_instance):
    result = network_instance.populate()
    assert 'interfaces' in result
    assert 'default_ipv4' in result
    assert 'default_ipv6' in result
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result
    assert result['interfaces'] == ['em0', 'em1']
    assert result['default_ipv4'] == {'interface': 'em0'}
    assert result['default_ipv6'] == {'interface': 'em1'}
    assert result['all_ipv4_addresses'] == []
    assert result['all_ipv6_addresses'] == []
    mock_merge_default_interface.assert_any_call({'interface': 'em0'}, {'em0': {'device': 'em0', 'type': 'ether'}, 'em1': {'device': 'em1', 'type': 'ether'}}, 'ipv4')
    mock_merge_default_interface.assert_any_call({'interface': 'em1'}, {'em0': {'device': 'em0', 'type': 'ether'}, 'em1': {'device': 'em1', 'type': 'ether'}}, 'ipv6')
