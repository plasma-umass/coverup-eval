# file lib/ansible/module_utils/facts/network/sunos.py:88-102
# lines [93]
# branches ['90->93', '96->98', '98->100']

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork

@pytest.fixture
def sunos_network(mocker):
    mocker.patch('ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.get_options', return_value=['LOOPBACK', 'IPv6'])
    module_mock = mocker.MagicMock()
    return SunOSNetwork(module=module_mock)

def test_parse_interface_line_with_ipv6_and_loopback(sunos_network):
    interfaces = {'lo0': {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}}
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,IPv6>', 'mtu', '8232']
    current_if = {}
    result_if = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result_if['device'] == 'lo0'
    assert result_if['type'] == 'loopback'
    assert 'ipv6' in result_if
    assert len(result_if['ipv6']) == 1
    assert result_if['ipv6'][0]['mtu'] == '8232'
    assert result_if['macaddress'] == 'unknown'
