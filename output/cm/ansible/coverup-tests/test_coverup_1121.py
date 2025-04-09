# file lib/ansible/module_utils/facts/network/aix.py:54-132
# lines [55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 116, 117, 118, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]
# branches ['66->67', '66->69', '71->73', '71->132', '73->74', '73->101', '77->78', '77->80', '80->81', '80->82', '82->83', '82->84', '84->85', '84->86', '86->87', '86->88', '88->89', '88->90', '90->91', '90->92', '92->93', '92->94', '94->95', '94->97', '101->71', '101->103', '103->104', '103->121', '105->106', '105->121', '107->108', '107->109', '109->110', '109->121', '110->111', '110->112', '113->114', '113->116', '117->109', '117->118', '121->71', '121->122', '123->71', '123->124', '125->126', '125->127', '127->71', '127->128', '128->127', '128->129', '130->127', '130->131']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, '0', ''),  # uname output
        (0, 'en0: flags=1e080863,843<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT\n'
            '        inet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255\n'
            '        inet6 abcd::1234 prefixlen 64\n'
            '        ether 00:0a:95:9d:68:16\n'
            '        media: Ethernet autoselect (1000baseT <full-duplex>)\n'
            '        status: active\n'
            '        lladdr 00:0a:95:9d:68:16\n', ''),  # ifconfig output
        (0, 'Hardware Address: 00:0a:95:9d:68:16\nDevice Type: Ethernet Network Interface\n', ''),  # entstat output
        (0, 'mtu 1500\n', '')  # lsattr output
    ])
    return mock_module

def test_get_interfaces_info(mock_module):
    aix_network = AIXNetwork(module=mock_module)
    interfaces, ips = aix_network.get_interfaces_info('/usr/sbin/ifconfig')

    assert interfaces['en0']['device'] == 'en0'
    assert interfaces['en0']['macaddress'] == '00:0a:95:9d:68:16'
    assert interfaces['en0']['type'] == 'ether'
    assert interfaces['en0']['mtu'] == '1500'
    assert '192.168.1.1' in ips['all_ipv4_addresses']
    assert 'abcd::1234' in ips['all_ipv6_addresses']
    assert mock_module.run_command.call_count == 4
