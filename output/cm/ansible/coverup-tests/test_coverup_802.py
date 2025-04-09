# file lib/ansible/module_utils/facts/network/generic_bsd.py:180-182
# lines [180, 181, 182]
# branches []

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_generic_bsd_ifconfig_network(mocker):
    mocker.patch.object(GenericBsdIfconfigNetwork, '__init__', return_value=None)
    return GenericBsdIfconfigNetwork()

def test_parse_ether_line(mock_generic_bsd_ifconfig_network):
    current_if = {}
    ips = []
    words = ['ether', '00:01:02:03:04:05']

    mock_generic_bsd_ifconfig_network.parse_ether_line(words, current_if, ips)

    assert current_if['macaddress'] == '00:01:02:03:04:05'
    assert current_if['type'] == 'ether'
