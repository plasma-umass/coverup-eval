# file lib/ansible/module_utils/facts/network/generic_bsd.py:156-170
# lines [157, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170]
# branches ['160->161', '160->162', '164->165', '164->168']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule(object):
    def __init__(self):
        self.params = {}

@pytest.fixture
def mock_generic_bsd_ifconfig_network(mocker):
    mocker.patch.object(GenericBsdIfconfigNetwork, 'get_options', return_value=['LOOPBACK'])
    mock_module = MockModule()
    return GenericBsdIfconfigNetwork(module=mock_module)

def test_parse_interface_line_with_loopback_and_newer_freebsd_version(mock_generic_bsd_ifconfig_network):
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '16384']
    expected_result = {
        'device': 'lo0',
        'ipv4': [],
        'ipv6': [],
        'type': 'loopback',
        'flags': ['LOOPBACK'],
        'macaddress': 'unknown',
        'metric': '0',
        'mtu': '16384'
    }
    result = mock_generic_bsd_ifconfig_network.parse_interface_line(words)
    assert result == expected_result

def test_parse_interface_line_with_loopback_and_older_freebsd_version(mock_generic_bsd_ifconfig_network):
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '16384']
    expected_result = {
        'device': 'lo0',
        'ipv4': [],
        'ipv6': [],
        'type': 'loopback',
        'flags': ['LOOPBACK'],
        'macaddress': 'unknown',
        'mtu': '16384'
    }
    result = mock_generic_bsd_ifconfig_network.parse_interface_line(words)
    assert result == expected_result
