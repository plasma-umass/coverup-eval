# file lib/ansible/module_utils/facts/network/sunos.py:88-102
# lines [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
# branches ['90->91', '90->93', '96->97', '96->98', '98->99', '98->100']

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetwork

@pytest.fixture
def sunos_network(mocker):
    mocker.patch('ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.get_options', return_value=['LOOPBACK', 'IPv6'])
    mocker.patch('ansible.module_utils.facts.network.base.Network.__init__', return_value=None)
    return SunOSNetwork(module=None)

def test_parse_interface_line_ipv6_loopback(sunos_network):
    interfaces = {}
    current_if = {}
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,IPv6>', 'mtu', '8232']
    
    result_if = sunos_network.parse_interface_line(words, current_if, interfaces)
    
    assert result_if['device'] == 'lo0'
    assert result_if['type'] == 'loopback'
    assert result_if['ipv6'] == [{'flags': ['LOOPBACK', 'IPv6'], 'mtu': '8232'}]
    assert result_if['macaddress'] == 'unknown'
